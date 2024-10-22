import requests
import base64
import json
from getpass import getpass

s1 = input("Introduzca el nombre del tenant:")
token = getpass("Introduzca token:")
s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"


headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}

with requests.Session() as s:
    i = s.get(s2,headers=headers1)
    print(i)

    print(json.dumps(i.json().get('Resources'),indent=4))

