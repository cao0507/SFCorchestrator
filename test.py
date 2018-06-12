import parse_request
import orchestrator

test = parse_request.jsonparser("sfc1")
vnfs = test.get_vnf_list()
cons = test.get_constrain_list()
print orchestrator.orchestrate(vnfs, cons)