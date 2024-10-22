import requests
import json

def getguid(s1,token,gp):
 s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups"
 headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}

 with requests.Session() as s:
    i = s.get(s2,headers=headers1)
    for x in i.json().get('Resources'):
     if x['displayName'] == gp:
      return(x['id'])
