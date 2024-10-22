import requests
import base64
import json
from getpass import getpass

def main():
    s1 = input("Introduzca el nombre del tenant:")
    token = getpass("Introduzca token:")
    s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups"
    group = input("Introduzca upn del grupo:")
    user_id = input("Introduzca ID del Usuario:")

    headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}

    payload = {
                    'schemas': ['urn:ietf:params:scim:schemas:core:2.0:Group'],
                    'displayName': group,
                    'members': [
                            {
                                    'value': user_id,
                            }
                            ],
                    'externalId': 'User-Ext_id',
                    'meta': {
                            'resourceType': 'Group'
                            }
            }

    with requests.Session() as s:
        i = s.post(s2,headers=headers1, data=json.dumps(payload))
        print(i)
