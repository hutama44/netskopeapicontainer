import requests
requests.packages.urllib3.disable_warnings()
import base64
import json
from getpass import getpass
import scim_abort

def main():
    success = 0
    s1 = input("Introduzca el nombre del tenant:")
    token = getpass("Introduzca token:")
    s2 = "https://" + s1 + ".goskope.com/api/v2/infrastructure/publishers"
    app = input("Introduzca nombre del publisher:")
    headers1 = {'Netskope-Api-Token':token, 'accept':'application/json'}

    with requests.Session() as s:
        i = s.get(s2,headers=headers1, verify=False) 
        for x in i.json().get('data').get('publishers'):
         if x['publisher_name'] == app:
          print(x['publisher_id'])
          success = 1
        if success != 1:
            scim_abort.main()

