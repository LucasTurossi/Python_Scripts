#!/usr/bin/python
import requests

site = requests.get("http://businesscorp.com.br")
status = site.status_code

if (status == 200):
    print ("GET 200")

else:
    print ("Page Down")
