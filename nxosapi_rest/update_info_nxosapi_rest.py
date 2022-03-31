from urllib import response
import requests
import json
from device_info import nxos
from pprint import pprint
from payload import payload

#speciy login url to capture token
url = f"https://{nxos['host']}/api/aaaLogin.json"

#data type to post
header = {
    'Content-Type':'application/json'
}
#send req to retieve token
response = requests.post(url,headers=header,auth=(nxos['username'],nxos['password']),data=payload,verify=False).json()
token = response['imdata'][0]['aaaLogin']['attributes']['token']
#store token in a dict
cookie = {}
cookie['APIC-cookie']=token
#specify the url of the obj to edit
url = f"https://{nxos['host']}/api/node/mo/sys/intf/lb-[lo199].json"
#open config data & send
with open('body') as f:
    body = f.read()
    response = requests.put(url,data=body,cookies=cookie,verify=False).json()
    print(response)