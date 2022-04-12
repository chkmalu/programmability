import requests
import json
from pprint import pprint

#specify the target url
url = "https://api.meraki.com/api/v0/organizations"

#api key to access resource
headers = {
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}
#send request to target url & convert to python obj with json()
response = requests.get(url,headers=headers).json()

orgid = ''
#loop 2ru to get the id of the organization
for org in response:
    if org['name'] == 'DevNet Sandbox':
        orgid = org['id']
print(orgid)