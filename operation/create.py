import json
import time

import sys
sys.path.append(r"/home/openstack/SFCorchestrator")

import api.tacker_api as tacker
from api.openstack_api import hypervisor
from parse_file.parse_request import jsonparser
from parse_file.configure_description_files import configure_file
import algorithm.mapper as mapper
import algorithm.orchestrator as orchestrator

def create(sfc_file):
    # instantiate work
    tacker_vnf = tacker.vnf()
    tacker_vnfd = tacker.vnfd()
    tacker_vnffg = tacker.vnffg()
    tacker_vnffgd = tacker.vnffgd()

    # Instantiation
    req = jsonparser(sfc_file)
    hypervisor_instance = hypervisor()
    conf = configure_file()
    
    sfc_name = req.get_sfc_name()  # The sfc name is the most important infomation!
    vnf_name_list = req.get_vnf_list()

    # Orchestration
    constrains = req.get_constrain_list()
    chain = orchestrator.orchestrate(vnf_name_list, constrains)

    # get the input of mapper algorithm
    sfc_detail = []
    for vnf in chain:
        vnf_detail = req.get_vnf_by_name(vnf)
        vnf_detail_brief = {}
        vnf_detail_brief["name"] = vnf_detail["name"]
        vnf_detail_brief["cpu"] = vnf_detail["flavor"]["cpu"]
        vnf_detail_brief["memory"] = vnf_detail["flavor"]["memory"]
        vnf_detail_brief["disk"] = vnf_detail["flavor"]["disk"]
        sfc_detail.append(vnf_detail_brief)
    objective = req.get_sfc_objective()
    hosts = hypervisor_instance.get_hosts_detail()

    # mapping
    sfc_mapper = {}  # used for create vnfds
    #mapper_output = {
    #    "vnf1":"nova:compute1",
    #    "vnf2":"nova:compute2"
    #}
    mapper_output = mapper.sfc_mapper(sfc_detail, hosts, objective)
    print mapper_output

    # configure vnfd files
    sfc_mapper = {}
    sfc_mapper["name"] = sfc_name
    sfc_mapper["mapper"] = mapper_output
    vnfd = []
    for vnf in vnf_name_list:
        vnf_detail = req.get_vnf_by_name(vnf)
        vnfd_file_name = conf.configure_vnfd(vnf_detail, sfc_mapper)
        vnfd.append(vnfd_file_name)
    
    # configure vnffgd file
    sfc_orchestrator = {}   # used for create vnffgd
    sfc_orchestrator["name"] = sfc_name
    sfc_orchestrator["chain"] = chain
    vnffgd_file = conf.configure_vnffgd(sfc_orchestrator)
    
    # create vnfds
    for vnfd_file in vnfd:
        tacker_vnfd.create_vnfd(vnfd_file)
    time.sleep(2)

    # create vnfs
    for vnf in vnf_name_list:
        vnf_name = sfc_name+ "_" + vnf
        vnfd_name = sfc_name + "_" + vnf + "_Description"
        vnfd_id = tacker_vnfd.get_vnfd_id(vnfd_name)
        tacker_vnf.create_vnf(vnf_name, vnfd_id)
        time.sleep(10)
        while tacker_vnf.get_vnf_status(vnf_name) != "ACTIVE":
            print "VNF:%s is being created!" % vnf_name
            time.sleep(5)
    
    # create vnffgd
    tacker_vnffgd.create_vnffgd(vnffgd_file)
    time.sleep(2)

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


if __name__ == "__main__":
    create("sfc1.json")
