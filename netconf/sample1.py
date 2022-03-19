from distutils.command.config import config
from ncclient import manager
import xmltodict
from pprint import pprint
from device_info import CSR1000V

# open filter file
with open('int-filter', 'r') as f:
  int_filter = f.read()
  # connect to client
  m = manager.connect(host=CSR1000V['host'],port=CSR1000V['port'],username=CSR1000V['username'],password=CSR1000V['password'],hostkey_verify=False)
  netcon = m.get(int_filter)
  # parse only data without rpc-reply into python ordered dict & print
  netdic = xmltodict.parse(netcon.xml)['rpc-reply']['data']
  print(f"Name:{netdic['interfaces']['interface']['name']['#text']}\n ip address:{netdic['interfaces']['interface']['ipv4']['address']['ip']}\n Netmask:{netdic['interfaces']['interface']['ipv4']['address']['netmask']}")
  print(f"status:{netdic['interfaces-state']['interface']['admin-status']}\n last-change:{netdic['interfaces-state']['interface']['last-change']}\n Mac-address:{netdic['interfaces-state']['interface']['phys-address']}")
  # pprint(netdic)
    # print(netcon)
    # for cap in m.server_capabilities:
    #     print('*' * 50)
    #     print(cap)
        # netcon = m.get(int_filter)
