import requests
import json
from getpass import getpass
import scim_abort
import datetime

def main():
    success = 0
    s1 = input("Introduzca el nombre del tenant:")
    user = input("Introduzca el upn:")
    token = getpass("Introduzca token:")
    s2 = "https://" + s1 + ".goskope.com/api/v2/ubadatasvc/user/uci"
    headers1 = {'Netskope-Api-Token':token,'accept':'application/json','Content-Type':'application/json'}
    rtime = input("Introduza fecha de inicio de búsqueda en formato d/m/y:" )
    ttime = datetime.datetime.strptime(rtime + " 00:00:00", "%d/%m/%Y %H:%M:%S").timestamp()
    ttime = str(ttime).replace(".","") + "00"
    data = {'fromTime':int(ttime),'user':user}
    print(ttime)
    with requests.Session() as s:
        i = s.post(s2,headers=headers1,data=json.dumps(data))
        print(i)
        print(i.text)

#    for x in i.json().get('Resources'):
#     if x['userName'] == us:
#      return(x['id'])
#    return("0")
