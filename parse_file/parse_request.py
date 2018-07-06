
"""
This moudle provides a series of encapsuled API
to parse the json file of SFC request.
"""

import json
import os
import sys
sys.path.append("/home/openstack/SFCorchestrator")
import config


class jsonparser(object):
    """The class is used to parse json file."""
    
    def __init__(self, filename):
        """Class initialization."""
        file_path = config.abs_dir
        f = open(file_path + "json/sfc/"+filename)
        self.req = json.load(f)
        f.close()

    def get_vnf_list(self):
        """Return the list of VNFs included SFC request."""
        return [vnf["name"] for vnf in self.req["VNF"]]

    def get_constrain_list(self):
        """Return the list of sequence constrains between VNFs."""
        return [[cons["former"], cons["later"]]
                for cons in self.req["constrain"]]

    def get_sfc_name(self):
        """Return the name of SFC."""
        return self.req["name"]

    def get_sfc_operation(self):
        """Return the expected operation. e.g. CREATE, DELETE and UPDATE."""
        return self.req["operation"]

    def get_vnf_by_name(self, name):
        """Return vnf details which is specified by its name."""
        for vnf in self.req["VNF"]:
            if vnf["name"] == name:
                return vnf

    def get_sfc_load(self):
        total = {"cpu": 0, "memory": 0, "disk": 0}
        for vnf in self.req["VNF"]:
            total["cpu"] += vnf["flavor"]["cpu"]
            total["memory"] += vnf["flavor"]["memory"]
            total["disk"] += vnf["flavor"]["disk"]
        return total

    def get_qos(self):
        return self.req["QoS"]

    def get_sfc_objective(self):
        return self.req["objective"]
