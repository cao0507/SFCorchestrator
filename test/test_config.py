from configure_file import configure_file
from parse_request import jsonparser

req = jsonparser('template_sfc')
conf = configure_file()
# az = "nova:compute1"
# vnf_list = req.get_vnf_list()
# for vnf in vnf_list:
#     conf.configure_vnfd(vnf, az)
sfc = {}
sfc["name"] = req.get_sfc_name()
chain = ["vnf2","vnf1","vnf3"]
sfc["chain"] = chain
conf.configure_vnffgd(sfc)


