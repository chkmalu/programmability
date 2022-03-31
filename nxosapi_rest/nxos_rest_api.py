import requests
import json
from device_info import nxos
from pprint import pprint
from payload import payload

#specify the login url
url = f"https://{nxos['host']}/api/aaaLogin.json"
#type of data to be post
login_header = {
    'Content-Type':'application/json'
}
#post req to retrieve token
response = requests.post(url,headers=login_header,data=payload,auth=(nxos['username'],nxos['password']),verify=False).json()
#parse response to get the token
token = response['imdata'][0]['aaaLogin']['attributes']['token']
#store token in a dict
cookie = {}
cookie['APIC-cookie']=token
#specify the url to get data
url = "https://sandbox-nxos-1.cisco.com/api/node/class/l3LbRtdIf.json"
#send req
res = requests.get(url,cookies=cookie,verify=False).json()
pprint(res)