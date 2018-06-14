import json
from parse_request import jsonparser
from mapper import mapper

class config_file(object):
    def __init__(self, file_name):
        #self.req = jsonparser(file_name)

    def config_vnfd(self)
        f = open("vnfd/template_vnfd.json", 'r')
        values = f.load(f)
        f.close()
        f = open("vnfd/vnfd" + vnf['num'] + ".json", 'w')
        
        f.close()

    #def config_vnffgd(self, vnffgd_file, INPUT)
