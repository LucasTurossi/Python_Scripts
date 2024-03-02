#!/usr/bin/python
import sys
from scapy.all import *

conf.verb = 0

ports = [21,22,25,53,80,443,3306,3389,8080,110]
pIP = IP(dst=sys.argv[1])
pTCP = TCP(dport=ports, flags="S")
packet = pIP/pTCP
resp, noresp = sr(packet)

for resposta in resp:
    porta = resposta[1][TCP].sport
    flag = resposta[1][TCP].flags
    if (flag == "SA"):
        print ("Porta %d OPEN" %(porta))
