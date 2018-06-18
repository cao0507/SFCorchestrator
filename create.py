import json
import tacker
from parse_request import jsonparser
from configure_file import configure_file
from mapper import mapper
import orchestrator
import time

def create(sfc_file):
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
    vnf_name_list = req.get_vnf_list()
    sfc_name = req.get_sfc_name()
    sfc_mapper = {}
    mapper_output = {
        "vnf1": "nova:compute2",
        "vnf2": "nova:compute1"
    }
    sfc_mapper["name"] = sfc_name
    sfc_mapper["mapper"] = mapper_output
    conf = configure_file()
    
    # configure vnfd file
    vnfd = []
    for vnf in vnf_name_list:
        vnf_detail = req.get_vnf_by_name(vnf)
        vnfd_file_name = conf.configure_vnfd(vnf_detail, sfc_mapper)
        vnfd.append(vnfd_file_name)
    
    # configute vnffgd file
    sfc_orchestrator = {}
    sfc_orchestrator["name"] = sfc_name
    constrains = req.get_constrain_list()
    chain = orchestrator.orchestrate(vnf_name_list, constrains)
    sfc_orchestrator["chain"] = chain
    vnffgd_file = conf.configure_vnffgd(sfc_orchestrator)
    
    # create vnfds
    for vnfd_file in vnfd:
        tacker_vnfd.create_vnfd(vnfd_file)

    # create vnfs
    for vnf in vnf_name_list:
        vnf_name = sfc_name+ "_" + vnf
        vnfd_name = sfc_name + "_" + vnf + "_Description"
        vnfd_id = tacker_vnfd.get_vnfd_id(vnfd_name)
        tacker_vnf.create_vnf(vnf_name, vnfd_id)
        time.sleep(30)
    
    # create vnffgd
    tacker_vnffgd.create_vnffgd(vnffgd_file)

    # create vnffg
    vnf_mapping = {}
    for vnf in vnf_name_list:
        vnf_name = sfc_name + "_" + vnf
        vnfd_name = sfc_name + "_" + vnf + "_Description"
        vnf_id = tacker_vnf.get_vnf_id(vnf_name)
        vnf_mapping[vnfd_name] = vnf_id
    vnffg_name = sfc_name + "_vnffg"
    vnffgd_name = sfc_name + "_vnffg_Description"
    vnffgd_id = tacker_vnffgd.get_vnffgd_id(vnffgd_name)
    tacker_vnffg.create_vnffg(vnffg_name, vnffgd_id, vnf_mapping)
    time.sleep(20)

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
    create("sfc1.json")
