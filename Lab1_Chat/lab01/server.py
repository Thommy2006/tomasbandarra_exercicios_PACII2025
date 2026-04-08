import socket
import threading
import logging
from gdpr_detector import (detect_personal_data, detect_social_engineering,
                            save_personal_data, save_social_engineering)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("server.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

HOST = "0.0.0.0"
PORT = 9999
ENCODING = "utf-8"
BUFFER_SIZE = 4096

clients: dict[socket.socket, str] = {}   # socket -> username
lock = threading.Lock()



def broadcast(message: str, exclude: socket.socket | None = None):
    """Send message to every connected client except *exclude*."""
    with lock:
        targets = [s for s in clients if s != exclude]
    for s in targets:
        _send(s, message)


def _send(sock: socket.socket, message: str):
    try:
        sock.send(message.encode(ENCODING))
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {e}")
        _remove(sock)


def _remove(sock: socket.socket) -> str | None:
    with lock:
        username = clients.pop(sock, None)
    try:
        sock.close()
    except Exception:
        pass
    return username


def _online_users(exclude: str = "") -> list[str]:
    with lock:
        return [u for u in clients.values() if u != exclude]


def _find_socket(username: str) -> socket.socket | None:
    with lock:
        for s, u in clients.items():
            if u == username:
                return s
    return None



def handle_client(sock: socket.socket, address):
    logging.info(f"Nova ligação de {address}")
    try:
        _send(sock, "[SERVER] Introduza o seu nome de utilizador: ")
        username = sock.recv(BUFFER_SIZE).decode(ENCODING).strip()

        with lock:
            taken = username in clients.values()

        if not username or taken:
            _send(sock, "[SERVER] Nome inválido ou já em uso. Ligação encerrada.\n")
            sock.close()
            return

        with lock:
            clients[sock] = username

        logging.info(f"Utilizador '{username}' ligado de {address}")
        broadcast(f"[SERVER] *** {username} entrou no chat! ***\n", exclude=sock)
        _send(sock, (
            f"[SERVER] Bem-vindo, {username}!\n"
            "  - 'exit'                        → sair\n"
            "  - '@utilizador <msg>'            → mensagem privada\n"
            "  - '!online'                      → listar utilizadores\n\n"
        ))

        online = _online_users(exclude=username)
        if online:
            _send(sock, f"[SERVER] Online agora: {', '.join(online)}\n\n")

        while True:
            try:
                raw = sock.recv(BUFFER_SIZE)
            except ConnectionResetError:
                break
            if not raw:
                break
            message = raw.decode(ENCODING).strip()
            if not message:
                continue

            # Exit
            if message.lower() == "exit":
                break

            if message.lower() == "!online":
                online = _online_users(exclude=username)
                _send(sock, f"[SERVER] Online: {', '.join(online) if online else 'ninguém mais'}\n")
                continue

            if message.startswith("@"):
                parts = message.split(" ", 1)
                target_name = parts[0][1:]
                content = parts[1] if len(parts) > 1 else ""
                _handle_dm(sock, username, target_name, content)
                continue

            _handle_broadcast(sock, username, message)

    except Exception as e:
        logging.error(f"Erro no handler de {address}: {e}")
    finally:
        uname = _remove(sock)
        if uname:
            logging.info(f"Utilizador '{uname}' desligado de {address}")
            broadcast(f"[SERVER] *** {uname} saiu do chat. ***\n")


def _gdpr_check(sock: socket.socket, username: str, message: str,
                context: str = "broadcast") -> bool:
    """Returns True if message is CLEAN (allowed), False if blocked."""
    detected = detect_personal_data(message)
    social   = detect_social_engineering(message)

    if detected:
        save_personal_data(username, message, detected)
        types = ", ".join(detected.keys())
        logging.warning(f"[GDPR] '{username}' ({context}) → {types} | '{message}'")
        _send(sock, f"[ALERTA GDPR] Mensagem bloqueada – dados pessoais detetados: {types}.\n")
        return False

    if social:
        save_social_engineering(username, message, social)
        logging.warning(f"[SOCIAL ENG] '{username}' ({context}) | '{message}'")
        _send(sock, "[AVISO] Mensagem identificada como possível engenharia social e registada.\n")
        return False

    return True


def _handle_broadcast(sock: socket.socket, username: str, message: str):
    if not _gdpr_check(sock, username, message, "broadcast"):
        return
    logging.info(f"[{username}] {message}")
    broadcast(f"[{username}] {message}\n", exclude=sock)


def _handle_dm(sock: socket.socket, sender: str, target: str, content: str):
    if not _gdpr_check(sock, sender, content, f"DM→{target}"):
        return
    target_sock = _find_socket(target)
    if target_sock:
        _send(target_sock, f"[DM de {sender}] {content}\n")
        _send(sock,        f"[DM para {target}] {content}\n")
        logging.info(f"[DM] {sender} → {target}: {content}")
    else:
        _send(sock, f"[SERVER] Utilizador '{target}' não encontrado ou offline.\n")



def start_server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(20)
    logging.info(f"Servidor iniciado em {HOST}:{PORT} – aguardando ligações...")

    try:
        while True:
            client_sock, address = srv.accept()
            t = threading.Thread(target=handle_client, args=(client_sock, address), daemon=True)
            t.start()
            logging.info(f"Thread iniciada para {address} | Clientes ativos: {threading.active_count() - 1}")
    except KeyboardInterrupt:
        logging.info("Servidor encerrado pelo utilizador (Ctrl+C).")
    finally:
        srv.close()


if __name__ == "__main__":
    start_server()
