import json
from parse_request import jsonparser

class configure_file(object):
    #def __init__(self, file_name):
    #    self.req = jsonparser(file_name)

    def configure_vnfd(self, vnf, sfc_mapper):  # sfc_mapper = {"name": "sfc1", "mapper": {"vnf1": "nova:compute2", "vnf2": "nova:compute1"}}
        f = open("vnfd/template_vnfd.json", 'r')
        vnfd_template = json.load(f)
        f.close()
        vnfd_template["vnfd"]["name"] = sfc_mapper["name"] + "_" +  vnf['name'] + "_Description"
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["capabilities"]["nfv_compute"]["properties"]["num_cpus"] = vnf["flavor"]["cpu"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["capabilities"]["nfv_compute"]["properties"]["mem_size"] = vnf["flavor"]["memory"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["capabilities"]["nfv_compute"]["properties"]["disk_size"] = vnf["flavor"]["disk"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["properties"]["image"] = vnf["type"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["properties"]["user_data"] = vnf["rule"]
        vnfd_template["vnfd"]["attributes"]["vnfd"]["topology_template"]["node_templates"]["VDU1"]["properties"]["availability_zone"] = sfc_mapper["mapper"][vnf["name"]]
        vnfd_file = sfc_mapper["name"] + "_" + vnf['name'] + "_Description.json"
        f = open("vnfd/" + vnfd_file, 'w')
        data = json.dumps(vnfd_template, sort_keys=True, indent=4, separators=(',',': '))
        f.write(data)
        f.close()
        return vnfd_file

    def configure_vnffgd(self, sfc_orchestrator):  # sfc_orchestrator = {"name": "sfc1", "chain": ["vnf2","vnf1","vnf3"] }
        f = open("vnffgd/template_vnffgd.json", 'r')
        vnffgd_template = json.load(f)
        f.close()

        path = []
        connection_point = []
        constituent_vnfs = []
        dependent_virtual_link = []
        for vnf in sfc["chain"]:
            path.append({"capability": "CP1", "forwarder": sfc_orchestrator["name"] + "_" + vnf + "_Description"})
            connection_point.append("CP1")
            constituent_vnfs.append(sfc_orchestrator["name"] + "_" + vnf + "_Description")
            dependent_virtual_link.append("VL1")

        vnffgd_template["vnffgd"]["name"] = sfc_orchestrator["name"] + "_vnffg_Description"
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["node_templates"]["Forwarding_path1"]["properties"]["path"] = path
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["connection_point"] = connection_point
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["constituent_vnfs"] = constituent_vnfs
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["dependent_virtual_link"] = dependent_virtual_link
        vnffgd_template["vnffgd"]["template"]["vnffgd"]["topology_template"]["groups"]["VNFFG1"]["properties"]["number_of_endpoints"] = len(sfc_orchestrator["chain"])       
        
        data = json.dumps(vnffgd_template, sort_keys=True, indent=4, separators=(',',': '))
        vnffgd_file = sfc_orchestrator["name"] + "_vnffg_Descrition.json"
        f = open("vnffgd/" + vnffgd_file, 'w')
        f.write(data)
        f.close()
        return vnffgd_file
