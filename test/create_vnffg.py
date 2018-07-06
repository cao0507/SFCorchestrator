import sys
sys.path.append(r"/home/openstack/SFCorchestrator")

import api.tacker_api as tacker

tacker_vnffg = tacker.vnffg()
tacker_vnffgd = tacker.vnffgd()

tacker_vnffgd.create_vnffgd("sfc1_vnffg_Description.json")

vnffg_name = "sfc1_vnffg"
vnf_mapping = {"sfc1_vnf1_Description": "6b8907ec-b66d-4cdc-ae29-41188e5d70d1"}
vnffgd_name = "sfc1_vnffg_Description"
vnffgd_id = tacker_vnffgd.get_vnffgd_id(vnffgd_name)
tacker_vnffg.create_vnffg(vnffg_name, vnffgd_id, vnf_mapping)
