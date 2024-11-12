import requests
import base64
import json
from getpass import getpass

def main():
        s1 = input("Introduzca el nombre del tenant:")
        token = getpass("Introduzca token:")
        user_upn = input("Introduzca UPN del Usuario:")
        resetuci(s1,token,user_upn)

def resetuci(s1,token,user_upn):
        s2 = "https://" + s1 + ".goskope.com/api/v2/incidents/users/uci/reset"
        headers1 = {'Netskope-Api-Token':token, 'accept': 'application/json','Content-Type': 'application/json'}
        payload = {
                        'users': [
                            user_upn
                            ]
                }

        with requests.Session() as s:
            i = s.post(s2,headers=headers1, data=json.dumps(payload))
            print(i)
            print(i.text)

