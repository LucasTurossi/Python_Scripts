import whois
import json
import re
import socket
import dns.resolver
import ssl
import flask 


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

    # Finding A record
result = dns.resolver.query(domain_name, 'A')
  
# Printing record
for val in result:
    print('A Record : ', val.to_text())

# Finding MX record
result = dns.resolver.query(domain_name, 'MX')
  
# Printing record
for val in result:
    print('MX Record : ', val.to_text())