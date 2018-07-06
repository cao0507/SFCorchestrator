import json
import sys
sys.path.append(r"/home/openstack/SFCorchestrator")

import api.tacker_api as tacker

tacker_vnf = tacker.vnf()
res = tacker_vnf.show_vnf("sfc1_vnf1")
print type(res)
print res
json_r = json.dumps(res, sort_keys=False, indent=4, separators=(',',': '))
print type(json_r)
print json_r

ip = tacker_vnf.get_vnf_ip("sfc1_vnf1")
print type(ip)
print ip
