import requests
import base64
import json
from getpass import getpass

def main():
    s1 = input("Introduzca el nombre del tenant:")
    token = getpass("Introduzca token:")
    s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"
    upn1 = input("Introduzca upn del usuario:")
    last_name = input("Introduzca apellido del usuario:")
    first_name = input("Introduzca nombre del usuario:")
    #true=true

    headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}

    payload = {
                    'schemas': ['urn:ietf:params:scim:schemas:core:2.0:User'],
                    'userName': upn1,
                    'name': {
                            'familyName': last_name,
                            'givenName': first_name
                            },
                    'active': 'true',
                    'emails': [
                            {
                                    'value': upn1,
                                    'primary': 'true'
                            }
                            ],
                    'externalId': 'User-Ext_id',
                    'meta': {
                            'resourceType': 'User'
                            }
            }

    with requests.Session() as s:
        i = s.post(s2,headers=headers1, data=json.dumps(payload))
        print(i)
