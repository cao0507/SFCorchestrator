import json
import tacker
from parse_request import jsonparser
from configure_file import configure_file
import mapper
import orchestrator
from openstack_api import hypervisor
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
    hypervisor_instance = hypervisor()
    conf = configure_file()

    vnf_name_list = req.get_vnf_list()
    constrains = req.get_constrain_list()
    chain = orchestrator.orchestrate(vnf_name_list, constrains)

    sfc_detail = []
    for vnf in vnf_name_list:
        vnf_detail = req.get_vnf_by_name(vnf)
        vnf_detail_brief = {}
        vnf_detail_brief["name"] = vnf_detail["name"]
        vnf_detail_brief["cpu"] = vnf_detail["flavor"]["cpu"]
        vnf_detail_brief["memory"] = vnf_detail["flavor"]["memory"]
        vnf_detail_brief["disk"] = vnf_detail["flavor"]["disk"]
        sfc_detail.append(vnf_detail_brief)
    target = req.get_sfc_target()
    hosts = hypervisor_instance.get_hosts_detail()
    mapper_output = mapper.sfc_mapper(sfc_detail, hosts, target)
    print mapper_output    

    sfc_name = req.get_sfc_name()
    sfc_mapper = {}
    sfc_mapper["name"] = sfc_name
    sfc_mapper["mapper"] = mapper_output
    

    # configure vnfd file
    vnfd = []
    for vnf in vnf_name_list:
        vnf_detail = req.get_vnf_by_name(vnf)
        vnfd_file_name = conf.configure_vnfd(vnf_detail, sfc_mapper)
        vnfd.append(vnfd_file_name)
    
    # configute vnffgd file
    sfc_orchestrator = {}
    sfc_orchestrator["name"] = sfc_name
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
        time.sleep(45)
    
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
    time.sleep(10)

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
