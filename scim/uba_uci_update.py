import requests
import base64
import json
from getpass import getpass
import datetime

def main():
        s1 = input("Introduzca el nombre del tenant:")
        token = getpass("Introduzca token:")
        user_upn = input("Introduzca UPN del Usuario:")
        user_uci = input("Introduzca infracción:")
        updateuci(s1,token,user_upn,user_uci)

def updateuci(s1,token,user_upn,user_uci):
        s2 = "https://" + s1 + ".goskope.com/api/v2/incidents/user/uciimpact"

        ts = datetime.datetime.today()
        ts = ts.timestamp()
        ts = str(ts).replace(".","")[:-3]
        print(ts)
        headers1 = {'Netskope-Api-Token':token, 'accept': 'application/json','Content-Type': 'application/json'}
        payload = {
                        'reason': 'Hugoapp input',
                        'score': int(user_uci),
                        'source': 'Hugoapp',
                        'timestamp': int(ts),
                        'user': user_upn
                }

        with requests.Session() as s:
            i = s.post(s2,headers=headers1, data=json.dumps(payload))
            print(i)

