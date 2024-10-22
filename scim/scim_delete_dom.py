import requests
import base64
import json
from getpass import getpass
from scim_del_domain import getuiddom

def main():
    s1 = input("Introduzca el nombre del tenant:")
    token = getpass("Introduzca token:")
    dom = input("Introduzca el dominio a eliminar:")

    ide = getuiddom(s1,token,dom)
    print(ide)
    for g in ide:
            s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users/" + g
            headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}
            with requests.Session() as s:
                i = s.delete(s2,headers=headers1)
                print(i.content)
