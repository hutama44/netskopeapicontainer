import requests
import base64
import json
from getpass import getpass
import scim_abort


def main():
    success = 0
    s1 = input("Introduzca el nombre del tenant:")
    us = input("Introduzca el upn:")
    token = getpass("Introduzca token:")
    s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"


    headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}

    with requests.Session() as s:
        i = s.get(s2,headers=headers1)
        print(i)

        for x in i.json().get('Resources'):
         if x['userName'] == us:
          print(json.dumps(x,indent=4))
          success=1
        if success != 1:
            scim_abort.main()

