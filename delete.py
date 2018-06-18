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

    vnf_name_list = tacker_vnf.list_vnf().keys()
    vnfd_name_list = tacker_vnfd.list_vnfd().keys()
    vnffg_name_list = tacker_vnffg.list_vnffg().keys()
    vnffgd_name_list = tacker_vnffgd.list_vnffgd().keys()
    
    
    # delete vnfs
    for vnf_name in vnf_name_list:
        if sfc_name in vnf_name:
            tacker_vnf.delete_vnf(vnf_name)
            time.sleep(30)

    # delete vnfds
    for vnfd_name in vnfd_name_list:
        if sfc_name in vnfd_name:
            tacker_vnfd.delete_vnfd(vnfd_name)
            time.sleep(5)

    # delete vnffg
    for vnffg_name in vnffg_name_list:
        if sfc_name in vnffg_name:
            tacker_vnffg.delete_vnffg(vnffg_name)
            time.sleep(20)

    # delete vnffgd
    for vnffgd_name in vnffgd_name_list:
        if sfc_name in vnffgd_name:
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


if __name__ == "__main__":
    delete("sfc1.json")
