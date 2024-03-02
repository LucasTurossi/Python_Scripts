import socket

def recv_all(sock):
    data = b''
    while True:
        part = sock.recv(4096)
        data += part
        if len(part) < 4096:
            break
    return data

# Solicitar informações do usuário
server_address = input("Digite o endereço ou hostname do servidor: ")
username = input("Digite o nome de usuário: ")

# Criação do socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp.connect((server_address, 21))
    print("Conectando ao servidor...")

    banner = tcp.recv(1024)
    print(banner.decode())

    tcp.send(str.encode(f"USER {username}\r\n"))
    user = tcp.recv(1024)
    print(user.decode())

    password = input("Digite a senha: ")
    tcp.send(str.encode(f"PASS {password}\r\n"))
    psswd = tcp.recv(1024)
    print(psswd.decode())

    while True:
        command = input("Digite um comando: ")
        tcp.send(str.encode(command + "\r\n"))
        response = recv_all(tcp)
        print(response.decode())

except socket.error as e:
    print("Erro ao conectar:", e)

finally:
    tcp.close()
