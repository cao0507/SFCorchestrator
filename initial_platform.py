import json
import parse_platform

def initial_platform(file_name):
    platform = parse_platform.jsonparser(file_name)
    service_ip = platform.get_service_ip()
    tenant_id = platform.get_tenant_id()
    user_id = platform.get_user_id()
    password = platform.get_password()

    # initial the service_ip in the identity.py file
    f = open("identity.py", "r")
    file_data = ""
    for line in f:
        if "service_ip =" in line:
            line = "service_ip = \"" +  service_ip + "\" \n"
        file_data += line
    f.close()
    f = open("identity.py", "w")
    f.write(file_data)
    f.close()

    # initial the tenant_id in the auth.json file
    f = open("auth.json", 'r')
    auth = json.load(f)
    f.close()
    auth["auth"]["identity"]["password"]["user"]["id"] = user_id
    auth["auth"]["identity"]["password"]["user"]["password"] = password
    auth["auth"]["scope"]["project"]["id"] = tenant_id
    f = open("auth.json", 'w')
    data = json.dumps(auth, sort_keys=True, indent=4, separators=(',',': '))
    f.write(data)
    f.close()

    # initial the service_ip in the openstack_api.py file
    f = open("openstack_api.py", "r")
    file_data = ""
    for line in f:
        if "service_ip =" in line:
            line = "service_ip = \"" +  service_ip + "\" \n"
        file_data += line
    f.close()
    f = open("openstack_api.py", "w")
    f.write(file_data)
    f.close()

    # initial the service_ip in the tacker.py file
    f = open("tacker.py", "r")
    file_data = ""
    for line in f:
        if "service_ip =" in line:
            line = "service_ip = \"" +  service_ip + "\" \n"
        file_data += line
    f.close()
    f = open("tacker.py", "w")
    f.write(file_data)
    f.close()

    # initial the tenant_id in the vnfd template file
#    f = open("vnfd/template_vnfd.json", 'r')
#    vnfd_template = json.load(f)
#    f.close()
#    vnfd_template["vnfd"]["tenant_id"] = tenant_id
#    f = open("vnfd/template_vnfd.json", 'w')
#    data = json.dumps(vnfd_template, sort_keys=True, indent=4, separators=(',',': '))
#    f.write(data)
#    f.close()
#
#    # initial the tenant_id in the vnffgd template file
#    f = open("vnffgd/template_vnffgd.json", 'r')
#    vnffgd_template = json.load(f)
#    f.close()
#    vnffgd_template["vnffgd"]["tenant_id"] = tenant_id
#    f = open("vnffgd/template_vnffgd.json", 'w')
#    data = json.dumps(vnffgd_template, sort_keys=True, indent=4, separators=(',',': '))
#    f.write(data)
#    f.close()

if __name__ == "__main__":
    initial_platform("platform.json")
