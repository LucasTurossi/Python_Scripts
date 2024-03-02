#!/usr/bin/python
import socket, sys

for port in range (1,65535):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if mysocket.connect_ex((sys.argv[1], port)) == 0:
        print ("Port", port, "[OPEN]")
        mysocket.close()