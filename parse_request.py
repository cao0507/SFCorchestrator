import json


class jsonparser(object):
    
    def __init__(self, filename):
        f = open("sfc/"+filename+".json")
        self.req = json.load(f)
        f.close()

    def get_vnf_list(self):
        return [vnf["name"] for vnf in self.req["VNF"]]

    def get_constrain_list(self):
        return [[cons["former"], cons["later"]]
                for cons in self.req["constrain"]]
