from urllib import response
import requests
import json
from pprint import pprint
from device_info import CSR1000V

url = f"https://{CSR1000V['host']}/restconf/data/Cisco-IOS-XE-native:native/router"

header = {
    'Content-Type':'application/yang-data+xml'
}
with open('ospf_config.xml') as f:
    ospfconfig = f.read()
    response = requests.post(url,headers=header,auth=(CSR1000V['username'],CSR1000V['password']),data=ospfconfig, verify=False)
    print(response.status_code)