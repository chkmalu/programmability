from opcode import hasnargs
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("10.10.20.110", "admin","ciscopsdt")
handle.login()

#get list of blade servers
blades = handle.query_classid("ComputeBlade")
for blade in blades:
    print(blade.dn,blade.serial,blade.total_memory)

handle.logout()
