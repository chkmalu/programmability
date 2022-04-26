from tokenize import Token
import requests
import json
from pprint import pprint

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

headers = {
  'Content-Type':'application/json'
  }

response = requests.post(url, headers=headers,auth=('devnetuser','Cisco123!')).json()
token = response['Token']

url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'

headers = {
    'x-auth-token': token
}

res = requests.get(url,headers=headers).json()
pprint(res)