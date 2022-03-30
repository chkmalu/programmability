from urllib import response
import requests
import json
from pprint import pprint
from device_info import nxos

url = f"https://{nxos['host']}/ins"

header = {
    'Content-Type':'application/json'
}

with open('get_tmp') as f:
    get_tmp = f.read()
    response = requests.post(url,headers=header,auth=(nxos['username'],nxos['password']),data=get_tmp,verify=False)

res = response.json()

for r in res['ins_api']['outputs']['output']['body']['TABLE_intf']['ROW_intf']:
    print(f"name:{r['intf-name']}----line_proto:{r['proto-state']}----linkf_state:{r['link-state']}----admin_state:{r['admin-state']}----ip_add:{r['prefix']}")
    print('#' * 100)