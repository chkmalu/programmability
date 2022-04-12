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
url = f"https://{aci['host']}/api/node/class/fvTenant.json"
#get list of tenants
get_resp = requests.get(url,headers=header,cookies=cookie,verify=False)
pprint(get_resp.json())