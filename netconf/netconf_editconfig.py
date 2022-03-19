from ncclient import manager
import xmltodict
from pprint import pprint
from device_info import CSR1000V

with open('edit_filter.xml', 'r') as f:
    edit_filter = f.read()
    edit_int = edit_filter.format(interface_name='Loopback69', interface_des='malu was here')
    m = manager.connect(host=CSR1000V['host'],port=CSR1000V['port'],username=CSR1000V['username'],password=CSR1000V['password'],hostkey_verify=False)
    device_reply = m.edit_config(edit_int, target="running")
    pprint(device_reply)