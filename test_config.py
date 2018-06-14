from config_file import config_file
from parse_request import jsonparser

req = jsonparser('template')
conf = config_file()
vnf_list = req.["VNF"]
for vnf in vnf_list:
    conf.config_vnfd(vnf)



