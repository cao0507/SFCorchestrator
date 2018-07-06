import json
import sys
sys.path.append("/home/openstack/SFCorchestrator")

from api.openstack_api import usage_reports

res = usage_reports().list_tenant_usage_statistics_for_all_tenants()
print type(res)
print res
json_r = json.dumps(res, indent=4, separators=(',','; '))
print type(json_r)
print json_r

sh_usage = usage_reports().show_usage_statistics_for_tenant("5ccb248ea8a0432c918eb09b1c4767ed")
json_sh = json.dumps(sh_usage, indent=4, separators=(',',';'))
f = open("show_usage.json", 'w')
f.write(json_sh)
f.close
print sh_usage
