import requests
import base64
import json
from getpass import getpass
import scim_get_guid

def main():
        s1 = input("Introduzca el nombre del tenant:")
        token = getpass("Introduzca token:")
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups/"
        group = input("Introduzca upn del grupo:")

        deletegroup(s1,token,s2,group)

def deletegroup(s1,token,s2,group):

        headers1 = {'Netskope-Api-Token':token, 'accept':'*/*'}
        print(s1,group)
        id=scim_get_guid.getguid(s1,token,group)
        with requests.Session() as s:
            i = s.delete(s2+id,headers=headers1)
            print(i)

