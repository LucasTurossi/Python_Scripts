#!/usr/bin/python
import socket, sys

host = sys.argv [1]

print (host, "=", socket.gethostbyname(host))