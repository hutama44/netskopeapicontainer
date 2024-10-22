import requests
import json
from getpass import getpass
from scim_get_uid import getuid
from scim_get_guid import getguid

def main():
    s1 = input("Introduzca el nombre del tenant:")
    token = getpass("Introduzca token:")
    upn = input("Introduzca upn del Usuario:")
    gp = input("Introduzca nombre del grupo:")

    user_id = getuid(s1,token,upn)
    group = getguid(s1,token,gp)
    s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups/" + group

    headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}

    payload = {
                    'schemas': ['urn:ietf:params:scim:api:messages:2.0:PatchOp'],
                    'Operations': [
                            {
                                    'path': 'members',
                                    'op': 'add',
                                    'value': {
                                            'value': {
                                                    'value': user_id,
                                                    }
                                            }
                            }
                            ],
            }

    with requests.Session() as s:
        i = s.patch(s2,headers=headers1, data=json.dumps(payload))
        print(i)
