import requests
import json

l = []
def getuiddom(s1,token,dom):
 s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"
 headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}
 with requests.Session() as s:
    i = s.get(s2,headers=headers1)
    for x in i.json().get('Resources'):
     if dom in x['userName']:
        l.append(x['id'])
    return(l)
