import parse_request

req = parse_request.jsonparser("template_sfc")

vnf_list = req.get_vnf_list()
print vnf_list
