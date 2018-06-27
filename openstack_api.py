
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

    
class server(object):
    """The class is about servers in the cloud platform."""
    
    def __init__(self):
        """Class initialization."""
        self.url = "http://" + service_ip + "/compute/v2.1/servers"
        self.requests = openstack_requests()

    def list_servers(self):
        """Return the list of servers."""
        r = self.requests.get(self.url).json()
        servers = r["servers"]
        for i in range(len(servers)):
            servers[i].pop("links")
        return servers

    def get_serverIP(self, id):
        """Return the IP address of the server with the id."""
        url = self.url + "/" + id + "/ips"
        r = self.requests.get(url).json()
        return r["addresses"]["private"][0]["addr"]

    def list_avaiable_server(self):
        """Return the list of servers can be used as source or destination."""
        servers = self.list_servers()
        available_servers = []
        for server in servers:
            if len(server["name"]) <= 10:
                server["IP"] = self.get_serverIP(server["id"])
                available_servers.append(server)
        return available_servers