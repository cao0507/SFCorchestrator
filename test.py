import parse_request
# import orchestrator

test = parse_request.jsonparser("sfc1")
# vnfs = test.get_vnf_list()
# cons = test.get_constrain_list()
# print orchestrator.orchestrate(vnfs, cons)

print test.get_vnf_list()
print test.get_constrain_list()
print test.get_sfc_name()
print test.get_sfc_operation()
print test.get_vnf_by_name("vnf1")
print test.get_sfc_load()
print test.get_qos()