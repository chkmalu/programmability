import requests
import json
from device_info import CSR1000V
from pprint import pprint

url = f"https://{CSR1000V['host']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback40"

header = {
    'Content-Type':'application/yang-data+json'
}

with open('body') as f:
    body = f.read()
    res = requests.put(url,headers=header,auth=(CSR1000V['username'],CSR1000V['password']),data=body,verify=False)
    print(res.status_code)