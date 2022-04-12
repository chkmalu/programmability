from urllib import response
import meraki
import json
from pprint import pprint

key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

dashboard = meraki.DashboardAPI(key)

orgs = dashboard.organizations.getOrganizations()
# pprint(orgs)

net = dashboard.networks.getNetwork('L_646829496481110568')
print(net)