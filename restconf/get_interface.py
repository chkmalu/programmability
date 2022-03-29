import requests
import json
from device_info import CSR1000V
from pprint import pprint

url = f"https://{CSR1000V['host']}/restconf/data/ietf-interfaces:interfaces/interface"

header = {
    'Accept':'application/yang-data+json'
}
#send req to device
response = requests.get(url, headers=header,auth=(CSR1000V['username'],CSR1000V['password']),verify=False)

res = response.json()
# pprint(res['ietf-interfaces:interface'])

def get_ip(r):
    try:
        for ip in r['ietf-ip:ipv4']['address']:
            print(f"ip:{ip['ip']}")
            print(f"mask:{ip['netmask']}")
            print("/" * 50)
    except KeyError:
        get_status(r)

def get_status(r):
    print(f"status:{r['enabled']}")

#get the interface details 
for r in res['ietf-interfaces:interface']:
    # pprint(r)
    # print('&' * 10)
    if 'description' in r:
        print(f"{r['name']}:{r['description']}")
        get_status(r)
        get_ip(r)
    elif 'address' not in r['ietf-ip:ipv4']:
        print(f"{r['name']}")
        get_status(r)
        print("/" * 50)
    else:
        print(f"{r['name']}")
        get_status(r)
        get_ip(r)