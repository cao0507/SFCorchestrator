import json
import tacker
import time
from parse_request import jsonparser

def delete(sfc_file):
    tacker_vnf = tacker.vnf()
    tacker_vnfd = tacker.vnfd()
    tacker_vnffg = tacker.vnffg()
    tacker_vnffgd = tacker.vnffgd()

    print "\n**************The VNFs list.****************"
    print tacker_vnf.list_vnf()
    print "\n**************The VNFDs list.****************"
    print tacker_vnfd.list_vnfd()
    print "\n**************The VNFFGs list.****************"
    print tacker_vnffg.list_vnffg()
    print "\n**************The VNFFGDs list.****************"
    print tacker_vnffgd.list_vnffgd()
    print "\n===================================================================="
    print "====================================================================\n"

    req = jsonparser(sfc_file)
    sfc_name = req.get_sfc_name()
    vnf_name_list = req.get_vnf_list()
    
    # delete vnfs and vnfds
    for vnf_name in vnf_name_list:
        tacker_vnf.delete_vnf(vnf_name)
        time.sleep(30)
        vnfd_name = sfc_name + "_" + vnf_name + "_Description"
        tacker_vnfd.delete_vnfd(vnfd_name)

    # delete vnffg and vnffgd
    vnffg_name = sfc_name + "_vnffg"
    vnffgd_name = sfc_name + "_vnffg_Description"
    tacker_vnffg.delete_vnffg(vnffg_name)
    time.sleep(20)
    tacker_vnffgd.delete_vnffgd(vnffgd_name)

    print "\n**************The VNFs list.****************"
    print tacker_vnf.list_vnf()
    print "\n**************The VNFDs list.****************"
    print tacker_vnfd.list_vnfd()
    print "\n**************The VNFFGs list.****************"
    print tacker_vnffg.list_vnffg()
    print "\n**************The VNFFGDs list.****************"
    print tacker_vnffgd.list_vnffgd()
    print "\n===================================================================="
    print "====================================================================\n"
