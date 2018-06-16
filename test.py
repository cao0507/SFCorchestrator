from parse_request import jsonparser
from tacker import vnf,vnfd,vnffg,vnffgd
from configure_file import configure_file
from mapper import mapper
import orchestrator
import time

aa = vnf()
bb = vnfd()
cc = vnffg()
dd = vnffgd()

vnfs = aa.list_vnf()
vnfds = bb.list_vnfd()
vnffgs = cc.list_vnffg()
vnffgds = dd.list_vnffgd()

print "****************The VNFs list.****************"
print vnfs
print "\n****************The VNFDs list.****************"
print vnfds
print "\n****************The VNFFGs list.****************"
print vnffgs
print "\n****************The VNFFGDs list.****************"
print vnffgds
print "\n====================================================================\n"

if vnfs.keys() is not []:
    for vnf_name in vnfs.keys():
        aa.delete_vnf(vnf_name)
        time.sleep(25)

if vnfds.keys() is not []:
    for vnfd_name in vnfds.keys():
        bb.delete_vnfd(vnfd_name)

if vnffgs.keys() is not []:
    for vnffg_name in vnffgs.keys():
        cc.delete_vnffg(vnffg_name)
        time.sleep(10)

if vnffgds.keys() is not []:
    for vnffgd_name in vnffgds.keys():
        dd.delete_vnffgd(vnffgd_name)


vnfs = aa.list_vnf()
vnfds = bb.list_vnfd()
vnffgs = cc.list_vnffg()
vnffgds = dd.list_vnffgd()

print "****************The VNFs list.****************"
print vnfs
print "\n****************The VNFDs list.****************"
print vnfds
print "\n****************The VNFFGs list.****************"
print vnffgs
print "\n****************The VNFFGDs list.****************"
print vnffgds
print "\n===================================================================="
print "====================================================================\n"

req = jsonparser('template_sfc')
vnf_list = req.get_vnf_list()
mapper = mapper()
mapper_output = mapper.mapper_func()
conf = configure_file()

# configure vnfd file
vnfd = []
for vnf in vnf_list:
    vnfd_file = conf.configure_vnfd(vnf, mapper_output[vnf["name"]])
    vnfd.append(vnfd_file)

# configure vnffgd file
sfc = {
    "name": "sfc1",
    "chain": ["vnf2", "vnf1"]
}
vnffgd_file = conf.configure_vnffgd(sfc)

# create vnfds
for vnfd_file in vnfd:
    bb.create_vnfd(vnfd_file)

# create vnfs
for vnf in vnf_list:
    aa.create_vnf(vnf["name"], vnf["name"]+"_Description")
    time.sleep(30)

# create vnffgd
dd.create_vnffgd(vnffgd_file)

# create vnffg
vnf_list_id = aa.list_vnf()
vnf_mapping = {}
for vnf in vnf_list:
    vnf_mapping[vnf["name"]] = vnf_list_id[vnf["name"]]

cc.create_vnffg(vnffg_name, vnffgd_name, vnf_mapping)


vnfs = aa.list_vnf()
vnfds = bb.list_vnfd()
vnffgs = cc.list_vnffg()
vnffgds = dd.list_vnffgd()

print "****************The VNFs list.****************"
print vnfs
print "\n****************The VNFDs list.****************"
print vnfds
print "\n****************The VNFFGs list.****************"
print vnffgs
print "\n****************The VNFFGDs list.****************"
print vnffgds
print "\n====================================================================\n"
