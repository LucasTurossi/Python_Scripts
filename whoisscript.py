#!/usr/bin/python
import whois
import socket
import dns.resolver
from flask import Flask

#Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__whoisscript__":
    app.run(debug=True)


# defining a function that returns a boolean indicating whwther a 'domain_name' is registered or not.
def is_registered(domain_name):
   try:
       w = whois.whois(domain_name)
   except Exception:
        return False
   else:
        return bool(w.domain_name)


if __name__ == '__main__':

 domain_name = input("Insira o domínio completo: ")
if is_registered(domain_name):

    whois_info = whois.whois(domain_name)
    # Print the creation date
    print("Data de criação do domínio: ", whois_info.creation_date)
    #print the expiration date
    print("O domínio expira no dia: ", whois_info.expiration_date)
    #Print status do domínio
    print("Status do domínio: ", whois_info.status)

#Get DNS entrys
dnsrecords=""
getresolver = dns.resolver.Resolver() 
getns = getresolver.resolve(domain_name, "NS") 
for rdata in getns:
    dnsrecords += str(rdata) + "\n"
print("DNS utlizado pelo domínio:\n", dnsrecords)

#Get A entry
domainip = socket.gethostbyname(domain_name)
print ("Apontamento em A domínio: \n", domainip)


#Get MX record
mailservers = "" 
for x in dns.resolver.resolve(domain_name, 'MX'): 
    mailservers += x.to_text() + "\n"
    trata = ""
    trata = mailservers.replace(" ","")
    trata = trata.replace("10","")
    trata = trata.replace("20","")
    trata = trata.replace("0","")
    trata = trata.replace("'","");  
    print("Entradas MX: \n", str(trata.replace (" ","")))
    spf = domain_name
    domain_name = trata[:-2]
    domain_name = socket.gethostbyname(domain_name)
print ("Apontamento IP do MX : ",domain_name)


#Get SPF and TXT entrys
textrecords = ""
getresolver = dns.resolver.Resolver()
    
try:
    gettext = getresolver.resolve(spf, "TXT") 
    for rdata in gettext: 
        textrecords += str(rdata) + "\n"
except:
    textrecords = "n/a"
print("Entradas SPF e TXT do domínio: \n",textrecords)
