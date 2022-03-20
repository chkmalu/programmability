from ncclient import manager
import xmltodict
from pprint import pprint
from device_info import CSR1000V

# open filter file
with open('filter.xml') as f:
  int_filter = f.read()
  # connect to client
  m = manager.connect(host=CSR1000V['host'],port=CSR1000V['port'],username=CSR1000V['username'],password=CSR1000V['password'],hostkey_verify=False)
  netcon = m.get(int_filter)
  # parse only data without rpc-reply into python ordered dict & print
  netdic = xmltodict.parse(netcon.xml)['rpc-reply']['data']
  ospf_prcs = netdic['native']['router']['ospf']
  prc_id = 0
  for prc in ospf_prcs:
      print(f"ospf-id:{prc['id']}")
      network = prc['network']
      if type(network) == list:
          for net in network:
              print(f"network:{net['ip']}")
              print(f"mask:{net['mask']}")
              print(f"area:{net['area']}")
              print('*' * 100)
      else:
          print(f"area:{network['area']}")
          print(f"network:{network['ip']}")
          print(f"mask:{network['mask']}")
          print('*' * 100)
      prc_id+=1