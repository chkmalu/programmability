import json
from socket import herror
from pkg_resources import invalid_marker
import requests
from device_info import CSR1000V
from pprint import pprint

url = f"https://{CSR1000V['host']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback40"

res = requests.delete(url,auth=(CSR1000V['username'],CSR1000V['password']),verify=False)
print(res.status_code)