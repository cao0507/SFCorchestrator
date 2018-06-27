
"""
This module initialize the cloud platform by
parsing json file of platform configuration
"""

import json
import config

import api.tacker_api as tacker

def initial_platform():
    """The fucntion executes a series of initial operations.

    :param file_name: the filename of platform configuration
    """
    # initial the tenant_id... in the auth.json file
    f = open("openstack_platform/auth.json", 'r')
    auth = json.load(f)
    f.close()
    auth["auth"]["identity"]["password"]["user"]["id"] = config.user_id
    auth["auth"]["identity"]["password"]["user"]["password"] = config.password
    auth["auth"]["scope"]["project"]["id"] = config.tenant_id
    f = open("openstack_platform/auth.json", 'w')
    data = json.dumps(auth, sort_keys=False, indent=4, separators=(',', ': '))
    f.write(data)
    f.close()

    # initial the auth_url... in the vim.json file
    f = open("openstack_platform/vim.json", 'r')
    vim_template = json.load(f)
    f.close()
    vim_template["vim"]["auth_cred"]["username"] = config.user_name
    vim_template["vim"]["auth_cred"]["password"] = config.password
    vim_template["vim"]["vim_project"]["name"] = config.tenant_name
    vim_template["vim"]["auth_url"] = "http://" + config.service_ip + "/identity" 
    f = open("openstack_platform/vim.json", 'w')
    data = json.dumps(vim_template, sort_keys=False, indent=4, separators=(',',': '))
    f.write(data)
    f.close()

    
    # initial the tenant_id in the vnfd template file
    f = open("json/tacker/vnfd/template_vnfd.json", 'r')
    vnfd_template = json.load(f)
    f.close()
    vnfd_template["vnfd"]["tenant_id"] = config.tenant_id
    f = open("json/tacker/vnfd/template_vnfd.json", 'w')
    data = json.dumps(vnfd_template, sort_keys=False, indent=4, separators=(',',': '))
    f.write(data)
    f.close()

    # initial the tenant_id in the vnffgd template file
    f = open("json/tacker/vnffgd/template_vnffgd.json", 'r')
    vnffgd_template = json.load(f)
    f.close()
    vnffgd_template["vnffgd"]["tenant_id"] = config.tenant_id
    f = open("json/tacker/vnffgd/template_vnffgd.json", 'w')
    data = json.dumps(vnffgd_template, sort_keys=False, indent=4, separators=(',',': '))
    f.write(data)
    f.close()

    # register the default VIM: Virtualized Infrastructure Manager
    tacker_vim = tacker.vim()
    default_vim = tacker_vim.get_default_vim()
    if default_vim is None:
        tacker_vim.register_vim("vim.json") 
    

if __name__ == "__main__":
    initial_platform()
