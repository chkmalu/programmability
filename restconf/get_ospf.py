import json
from urllib import response
import requests
from pprint import pprint
from device_info import CSR1000V

url = f"https://{CSR1000V['host']}/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:ospf"

header = {
    'Accept':'application/yang-data+json'
}

response = requests.get(url,headers=header,auth=(CSR1000V['username'],CSR1000V['password']),verify=False)
res = response.json()


def params(r):
    print(f"ospf_id:{r['id']}")
    try:
        for ip_add in r['network']:
            print(f"ip address:{ip_add['ip']}\nnetmask:{ip_add['mask']}\narea:{ip_add['area']}")
            print('#' * 40)
    except KeyError:
        pass

for r in res['Cisco-IOS-XE-ospf:ospf']:
    params(r)