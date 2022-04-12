import requests
import json
from device_info import aci
from pprint import pprint

#url for login
url = f"https://{aci['host']}/api/aaaLogin.json"

header = {
    'Contect-Type':'application/json'
}
#login details
payload = {
    "aaaUser":{
        "attributes":{
            "name":f"{aci['username']}",
            "pwd":f"{aci['password']}"
        }
    }
}
#get token
response = requests.post(url,headers=header,data=json.dumps(payload),verify=False).json()
# pprint(response)

# parse data to get token
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] =token

header = {
    'Accept':'application/json'
}
#create tenant
payload = {
    "fvTenant":{
        "attributes":{
            "dn":"uni/tn-malutek",
            "name":"malutek",
            "rn":"tn-malutek",
            "status":"created"},
            "children":[]
            }
            }
#target obj to url to configure
url = f"https://{aci['host']}/api/node/mo/uni/tn-malutek.json"
#get list of tenants
get_resp = requests.post(url,headers=header,data=json.dumps(payload),cookies=cookie,verify=False)
pprint(get_resp)