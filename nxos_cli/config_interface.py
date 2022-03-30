from distutils.command.config import config
from urllib import response
import requests
import json
from device_info import nxos
from pprint import pprint

url = f"https://{nxos['host']}/ins"

header = {
    'Content-Type':'application/json'
}

with open('config_tmp') as f:
    config_tmp = f.read()
    response = requests.post(url,headers=header,data=config_tmp,auth=(nxos['username'],nxos['password']),verify=False)
    print(response.status_code)