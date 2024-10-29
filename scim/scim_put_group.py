import requests
import base64
import json
from getpass import getpass
import scim_get_uid

def main():
        s1 = input("Introduzca el nombre del tenant:")
        token = getpass("Introduzca token:")
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups"
        group = input("Introduzca upn del grupo:")
        user_upn = input("Introduzca UPN del Usuario:")

        creategroup(s1,token,s2,group,user_upn)

def creategroup(s1,token,s2,group,user_upn):

        headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}
        user_id = scim_get_uid.getuid(s1,token,user_upn)

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

