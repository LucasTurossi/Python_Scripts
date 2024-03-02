#!/usr/bin/python
import socket,sys


if len(sys.argv) !=3:
    print("Modo de uso:")
    print("python SMTP_Enum.py host user")
    sys.exit(0)

print("Alvo", sys.argv[1])
print("")
print("Estabelecendo conexão:")
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],25))
banner = tcp.recv(1024)
print (banner)

tcp.send(str.encode("VRFY "+sys.argv[2]+"\r\n"))
user= tcp.recv(1024)
print(user )