from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from pprint import pprint

auth = Authentication(host='10.10.20.90',user='admin',password='C1sco12345',validate_certs=False).login()
vmdevice = Device(session=auth,host='10.10.20.90')
device_list = vmdevice.get_device_list('Any')
for device in device_list:
    pprint(device)