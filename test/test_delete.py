import sys
sys.path.append(r"/home/openstack/SFCorchestrator")

import api.tacker_api as tacker

tacker_vnffg = tacker.vnffg()
tacker_vnffgd = tacker.vnffgd()

tacker_vnffgd.delete_vnffgd("sfc1_vnffg_Description")
tacker_vnffg.delete_vnffg("sfc1_vnffg")
