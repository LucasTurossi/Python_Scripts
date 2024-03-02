#!/usr/bin/python

import socket

ip = input("Digite o endereço de IP:")
port = int(input("Digite a porta:"))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((ip, port))
banner = mysocket.recv(1024)
print (banner)