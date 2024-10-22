import requests
import base64
import json
from getpass import getpass
from scim_get_uid import getuid

def main():
    s1 = input("Introduzca el nombre del tenant:")
    token = getpass("Introduzca token:")
    upn = input("Introduzca el upn del usuario:")

    ide = getuid(s1,token,upn)
    s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users/" + ide

    headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}

    with requests.Session() as s:
        i = s.delete(s2,headers=headers1)
        print(i.content)
