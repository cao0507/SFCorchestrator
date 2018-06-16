import json


class jsonparser(object):
    
    def __init__(self, filename):
        f = open("sfc/"+filename+".json")
        self.req = json.load(f)
        f.close()

    def get_vnf_list(self):
        #return [vnf["name"] for vnf in self.req["VNF"]]
        return self.req["VNF"]

    def get_constrain_list(self):
        return [[cons["former"], cons["later"]]
                for cons in self.req["constrain"]]

    def get_sfc_name(self):
        return self.req["name"]

    def get_sfc_operation(self):
        return self.req["operation"]

    def get_vnf_by_name(self, name):
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
