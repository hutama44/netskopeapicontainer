import requests
import json

def getuid(s1,token,us):
 s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"
 headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}
 with requests.Session() as s:
    i = s.get(s2,headers=headers1)
    for x in i.json().get('Resources'):
     if x['userName'] == us:
      return(x['id'])
    return("0")
