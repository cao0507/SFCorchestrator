
"""This module provides a series of encapsuled openstack APIs"""

from openstack_requests import openstack_requests

service_ip = "192.168.1.30" 


class hypervisor(object):
    """The class is about hypervisors of cloud platform."""

    def __init__(self):
        """Class initialization."""
        self.url = "http://" + service_ip + "/compute/v2.1/os-hypervisors"
        self.requests = openstack_requests()

    def get_hosts_detail(self):
        """The function gets the state of hosts."""
        url = self.url + "/detail"
        r = self.requests.get(url).json()
        hosts = []
        for hypervisor in r["hypervisors"]:
            host = {}
            host["name"] = "nova:"+hypervisor["hypervisor_hostname"]
            host["cpu"] = hypervisor["vcpus"] - hypervisor["vcpus_used"]
            host["memory"] = hypervisor["free_ram_mb"]
            host["disk"] = hypervisor["free_disk_gb"]
            hosts.append(host)
        return hosts
