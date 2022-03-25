from ncclient import manager
import xmltodict
from pprint import pprint
from device_info import CSR1000V
from ip_address import network

#open rpc template & connect to the device
with open('edit_filter.xml') as f:
    edit_filter = f.read()
    m = manager.connect(host=CSR1000V['host'],port=CSR1000V['port'],username=CSR1000V['username'],password=CSR1000V['password'],hostkey_verify=False)
#pass in the place holder & send config
    for ip in network['ip']:
        adv_net = edit_filter.format(ip_add=ip['ip_address'],netmask=ip['mask'])
        # print(adv_net)
        device_reply = m.edit_config(adv_net, target="running")
        pprint(device_reply)