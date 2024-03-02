#!/usr/bin/python
import socket, sys,re

if len(sys.argv) !=2:
    print("Modo de uso:")
    print("python SMTP_Enum.py target")
    sys.exit(0)

file = open("path to file")
for user in file:
    tcp =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((sys.argv[1], 25))
    banner = tcp.recv(1024)
    tcp.send(str.encode("VRFY " +user))
    response = tcp.recv(1024).decode('utf-8')
    if re.search("252", response):
        print("Usuário encontrado: "+response.strip("252 2.0.0"))
