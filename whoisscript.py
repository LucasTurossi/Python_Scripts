import whois
import json
import re
import socket
import dns.resolver
import ssl
import flask 
from io import StringIO
import sys


# defining a function that returns a boolean indicating whwther a 'domain_name' is registered or not.
def is_registered(domain_name):
   try:
       w = whois.whois(domain_name)
   except Exception:
        return False
   else:
        return bool(w.domain_name)


if __name__ == '__main__':

 domain_name = input("Please enter any domain name: ")
if is_registered(domain_name):

    whois_info = whois.whois(domain_name)
    #print the name of registrar
    print("DOMAIN REGISTRAR: ",whois_info.registrar)
    # print the WHOIS server
    print("WHOIS SERVER: ", whois_info.whois_server)
    # Print the creation date
    print("Domain Creation Date: ",whois_info.creation_date)
    #print the expiration date
    print("Expiration Date: ", whois_info.expiration_date)
    print("MX ", whois_info.mx)
    #print all information related to whois
    print(whois_info)

#Get entrada em A

domainip = socket.gethostbyname(domain_name)
print (domainip)

#Get MX record

mailservers = "" 
for x in dns.resolver.resolve(domain_name, 'MX'): 
    mailservers += x.to_text() + "\n"
print(mailservers)

#Get SPF and TXT entrys

textrecords = ""
getresolver = dns.resolver.Resolver()
    
try:
    gettext = getresolver.resolve(domain_name, "TXT") 
    for rdata in gettext: 
        textrecords += str(rdata) + "\n"
except:
    textrecords = "n/a"
print(textrecords)

domainip = socket.gethostbyname(domain_name)
print (domainip)


#Get print output and convert to a variable
