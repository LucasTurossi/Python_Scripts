#!/usr/bin/python
import socket, sys
print ("FTP Connection\n")
ip = input("Digite o alvo (IP, domain ou host):") 
port = 21

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((ip, port))
banner = mysocket.recv(1024)
print (banner)

print("Enviando User\n")
mysocket.send(str.encode('USER teste\r\n'))
banner = mysocket.recv(1024)
print (banner)

print("Enviando senha\n")
mysocket.send(str.encode('PASS teste\r\n'))
banner = mysocket.recv(1024)
print (banner)