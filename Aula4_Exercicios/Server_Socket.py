# ==========================================
# SERVIDOR TCP EM PYTHON
# SOCKET SERVER
# ==========================================

import socket     # biblioteca para comunicação em rede
import time       # biblioteca para controlo de tempo


# -------------------------------
# 1. CRIAR SOCKET DO SERVIDOR
# -------------------------------
# AF_INET  -> usa IPv4
# SOCK_STREAM -> usa protocolo TCP

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# -------------------------------
# 2. DEFINIR IP E PORTA
# -------------------------------

host = "127.0.0.1"   # localhost
porta = 12340        # porta do servidor


# -------------------------------
# 3. BIND (VÍNCULO)
# -------------------------------
# Associa a socket ao IP e à porta

serverSocket.bind((host, porta))


# -------------------------------
# 4. LISTEN (ESPERAR CONEXÕES)
# -------------------------------
# listen(1) -> permite 1 cliente em espera

serverSocket.listen(1)

print(f"Servidor ligado em {host}:{porta}")
print("A aguardar conexão de cliente...")


# -------------------------------
# 5. ACEITAR CONEXÃO DO CLIENTE
# -------------------------------
# accept() devolve:
# clientsocket -> socket do cliente
# enderecoCliente -> IP e porta do cliente

clientSocket, enderecoCliente = serverSocket.accept()

print(f"Conexão estabelecida com {enderecoCliente}")


# Loop para comunicação contínua
while True:
    # -------------------------------
    # 6. RECEBER MENSAGEM DO CLIENTE
    # -------------------------------
    # recv(1024) -> recebe até 1024 bytes
    # decode() -> converte bytes para string

    mensagem = clientSocket.recv(1024).decode()
    
    # Verificar se o cliente fechou a conexão
    if not mensagem:
        print("Cliente desconectou-se.")
        break
        
    print("Mensagem recebida:", mensagem)
    
    # Verificar se a mensagem é "adeus"
    if mensagem.lower() == "adeus":
        print("Cliente disse adeus. A encerrar conexão...")
        resposta = "adeus"
        clientSocket.send(resposta.encode())
        break

    # -------------------------------
    # 7. ENVIAR RESPOSTA AO CLIENTE
    # -------------------------------
    # encode() -> converte string para bytes

    resposta = input("Servidor: ")  # Alterado para permitir resposta do servidor
    clientSocket.send(resposta.encode())
    
    # Verificar se o servidor disse "adeus"
    if resposta.lower() == "adeus":
        print("Servidor disse adeus. A encerrar conexão...")
        break


# -------------------------------
# 8. ESPERA (SIMULA PROCESSAMENTO)
# -------------------------------

time.sleep(2)


# -------------------------------
# 9. FECHAR CONEXÕES
# -------------------------------

clientSocket.close()
serverSocket.close()

print("Conexões fechadas.")