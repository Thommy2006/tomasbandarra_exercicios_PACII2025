import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 9999
ENCODING = "utf-8"
BUFFER_SIZE = 4096

stop_event = threading.Event()


def receive_loop(sock: socket.socket):
    """Background thread: print everything the server sends."""
    while not stop_event.is_set():
        try:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                print("\n[INFO] Ligação encerrada pelo servidor.")
                stop_event.set()
                break
            print(data.decode(ENCODING), end="", flush=True)
        except OSError:
            if not stop_event.is_set():
                print("\n[ERRO] Ligação perdida com o servidor.")
            stop_event.set()
            break
        except Exception as e:
            if not stop_event.is_set():
                print(f"\n[ERRO] {e}")
            stop_event.set()
            break


def start_client():
    global HOST, PORT

    if len(sys.argv) > 1:
        HOST = sys.argv[1]
    if len(sys.argv) > 2:
        PORT = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"[ERRO] Não foi possível conectar a {HOST}:{PORT}")
        sys.exit(1)

    print(f"[INFO] Conectado ao servidor {HOST}:{PORT}")
    print("[INFO] Comandos: 'exit' | '!online' | '@user <msg>' para DM\n")

    recv_thread = threading.Thread(target=receive_loop, args=(sock,), daemon=True)
    recv_thread.start()

    try:
        while not stop_event.is_set():
            try:
                msg = input()
            except EOFError:
                break
            if stop_event.is_set():
                break
            if not msg.strip():
                continue
            try:
                sock.send(msg.encode(ENCODING))
            except OSError:
                print("[ERRO] Falha ao enviar mensagem.")
                break
            if msg.strip().lower() == "exit":
                stop_event.set()
                break
    except KeyboardInterrupt:
        print("\n[INFO] A encerrar...")
        try:
            sock.send("exit".encode(ENCODING))
        except Exception:
            pass
    finally:
        stop_event.set()
        sock.close()
        print("[INFO] Desligado do servidor.")


if __name__ == "__main__":
    start_client()
