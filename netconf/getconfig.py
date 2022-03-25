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
  # pprint(netdic)
  ospf_prcs = netdic['native']['router']['ospf']
  pprint(ospf_prcs)

  def ospf_params(nwt):
      print(f"area:{nwt['area']}")
      print(f"network:{nwt['ip']}")
      print(f"mask:{nwt['mask']}")
      print('*' * 100)

  for prc in ospf_prcs:
      print(f"ospf-id:{prc['id']}")
      try:
          network = prc['network']
      except KeyError:
          print('NO network advertised')
          pass
      if type(network) == list:
          for net in network:
              ospf_params(net)
      else:
          ospf_params(network)