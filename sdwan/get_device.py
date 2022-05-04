import requests
import json 
from pprint import pprint

url = "https://10.10.20.90:443/j_security_check"

login = {
    'j_username':'admin',
    'j_password':'C1sco12345'
}
#maintain SD-WAN session 
session = requests.session()

response = session.post(url,data=login,verify=False)
#verify login
if not response.ok or response.text:
    print('login fail')
    import sys
    sys.exit(1)
else:
    print('login worked')
#get list of devices
url = url = "https://10.10.20.90:443/dataservice/device"

device_resp = session.get(url,verify=False).json()['data']
# pprint(device_resp)

for device in device_resp:
    print(f"HOSTNAME:{device['host-name']}")
    print(f"IP_ADD{device['local-system-ip']}")
    print(f"MODEL:{device['device-model']}")
    print(f"STATE:{device['status']}")
    print(' ')