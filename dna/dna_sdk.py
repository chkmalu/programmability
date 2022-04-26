from dnacentersdk import DNACenterAPI
import json
from pprint import pprint

#establish connection to controller
api = DNACenterAPI(username='devnetuser',password='Cisco123!',base_url='https://sandboxdnac.cisco.com',version='1.2.10',verify=False)
#get list of all devices
devices = api.devices.get_device_list()
#get deviceid of a particular device
deviceid = devices['response'][0]['id']
#get the all interface info of all the device for the above deviceid
ints = api.devices.get_interface_info_by_id(device_id=deviceid)
pprint(ints)