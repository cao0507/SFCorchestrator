
"""
This module will configure both VNFD file and VNFFGD file
according to the SFC request and the orchestration result.
"""

import json
import random
import os
import sys
sys.path.append(r"/home/openstack/SFCorchestrator")

import config


class configure_file(object):
    """The class includes a series of configuration actions."""
    def __init__(self):
        self.file_path = os.path.abspath('.')

    def configure_vnfd(self, vnf, sfc_mapper):
        """The function will configure VNFD file.

        :param vnf: the list of vnfs to be created
        :param sfc_mapper: the dictionary includes SFC's name
        and mapping hosts of each vnf. e.g. sfc_mapper = {"name": "sfc1",
        "mapper":{"vnf1": "nova:compute2", "vnf2": "nova:compute1"}}
        :returns: the filename of configured VNFD
        """
        # read vnf_template from json file
        f = open(self.file_path + "/json/tacker/vnfd/template_vnfd.json", 'r')
        vnfd_template = json.load(f)
        f.close()
        if vnf["type"] == "FW_image":
            user_data = "#!/bin/bash\n echo 'FW user_data import successfully!' > /home/openstack/test.log\n %s " % vnf["rule"]
        elif vnf["type"] == "IDS_image":
            user_data = "#!/bin/bash\n echo 'IDS user_data import successfully!' > /home/openstack/test.log\n rm /etc/snort/rules/local.rules\n echo %s >/etc/snort/rules/local.rules\n snort -T -c /etc/snort/snort.conf -i eth0\n /usr/local/bin/snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i eth0 >/home/openstack/snort.log" % vnf["rule"]
        vnfd_template["vnfd"]["tenant_id"] = config.tenant_id
        vnfd_template["vnfd"]["name"] = sfc_mapper["name"] + "_" +  vnf['name'] + "_Description"
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["capabilities"]["nfv_compute"]["properties"]["num_cpus"] = vnf["flavor"]["cpu"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["capabilities"]["nfv_compute"]["properties"]["mem_size"] = str(vnf["flavor"]["memory"]) + " MB"
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["capabilities"]["nfv_compute"]["properties"]["disk_size"] = str(vnf["flavor"]["disk"]) + " GB"
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["properties"]["image"] = vnf["type"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["properties"]["user_data"] = user_data
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["properties"]["availability_zone"] = sfc_mapper["mapper"][vnf["name"]]
        vnfd_file = sfc_mapper["name"] + "_" + vnf['name'] + "_Description.json"

        f = open(self.file_path + "/json/tacker/vnfd/" + vnfd_file, 'w')
        data = json.dumps(vnfd_template, sort_keys=False, indent=4, separators=(',',': '))
        f.write(data)
        f.close()
        
        return vnfd_file

    def configure_vnffgd(self, sfc_orchestrator):
        """The function will configure VNFFGD file.

        :param sfc_orchestrator: the dictionary includes the sfc name
        and the orchestrated vnfs of the sfc. e.g. sfc_orchestrator =
        {"name": "sfc1", "chain": ["vnf2","vnf1","vnf3"] } 
        """
        # read vnffg_template from json file
        f = open(self.file_path + "/json/tacker/vnffgd/template_vnffgd.json", 'r')
        vnffgd_template = json.load(f)
        f.close()

        # construct VNFFG according to sfc_orchestrator
        path = []
        connection_point = []
        constituent_vnfs = []
        dependent_virtual_link = []
        for vnf in sfc_orchestrator["chain"]:
            path.append({"capability": "CP1", "forwarder":
                        sfc_orchestrator["name"] + "_" + vnf + "_Description"})
            connection_point.append("CP1")
            constituent_vnfs.append(sfc_orchestrator["name"]
                                    + "_" + vnf + "_Description")
            dependent_virtual_link.append("VL1")

        # update VNNFGD 
        vnffgd_template["vnffgd"]["tenant_id"] = config.tenant_id
        vnffgd_template["vnffgd"]["name"] = \
            sfc_orchestrator["name"] + "_vnffg_Description"
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["description"] = \
            sfc_orchestrator["name"] + "vnffg" 
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["node_templates"]["Forwarding_path1"]["properties"]["policy"]["criteria"][0]["network_src_port_id"] = config.src_port_id
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["node_templates"]["Forwarding_path1"]["properties"]["policy"]["criteria"][0]["ip_dst_prefix"] = config.dst_ip
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["node_templates"]["Forwarding_path1"]["properties"]["path"] = path
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["node_templates"]["Forwarding_path1"]["properties"]["id"] = random.randint(1, 100)
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["connection_point"] = connection_point
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["constituent_vnfs"] = constituent_vnfs
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["dependent_virtual_link"] = dependent_virtual_link
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["number_of_endpoints"] = len(sfc_orchestrator["chain"])       

        # write VNNFGD into file
        data = json.dumps(vnffgd_template,
                          sort_keys=False, indent=4, separators=(',', ': '))
        vnffgd_file = sfc_orchestrator["name"] + "_vnffg_Descrition.json"
        f = open(self.file_path + "/json/tacker/vnffgd/" + vnffgd_file, 'w')
        f.write(data)
        f.close()
        
        return vnffgd_file
