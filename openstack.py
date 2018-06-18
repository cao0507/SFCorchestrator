import json
import identity
from openstack_requests import openstack_requests


class hepervisor(object):
    def __init__(self):
        self.url = "http://192.168.1.30/compute/v2.1/os-hypervisors"
        self.requests = openstack_requests()

    def get_hosts_detail(self):
        url = self.url + "/detail"
        r = self.requests.get(url).json()
        hosts = []
        for hypervisor in r["hypervisors"]:
            host = {}
            host["name"] = "nava:"+hypervisor["hypervisor_hostname"]
            host["cpu"] = hypervisor["vcpus"] - hypervisor["vcpus_used"]
            host["memory"] = hypervisor["free_ram_mb"]
            host["disk"] = hypervisor["free_disk_gb"]
            hosts.append(host)
        return hosts