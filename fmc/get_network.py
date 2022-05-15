import requests
import json
from pprint import pprint

base_url = "https://fmcrestapisandbox.cisco.com/"
login_url = "api/fmc_platform/v1/auth/generatetoken"

header = {
    'Content-Type':'application/json'
}
username = 'chikamaluj'
password = 'J6yzcJnd'
#login to get token for authenication
login_resp = requests.post(f'{base_url}{login_url}',headers=header,auth=(username, password),verify=False)
#parse the token
header_resp = login_resp.headers
token = header_resp.get('X-auth-access-token')
header['X-auth-access-token'] = token

#api url to get list of networks
network_url = 'api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks'
#get list of network
get_network = requests.get(f'{base_url}{network_url}',headers=header,auth=(username,password),verify=False).json()
pprint(get_network)