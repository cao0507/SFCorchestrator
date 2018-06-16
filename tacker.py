import json
import identity
from openstack_requests import openstack_requests


class vnf(object):
    def __init__(self):
        self.url = "http://192.168.1.91:9890/v1.0/vnfs"
        self.requests = openstack_requests()

    def list_vnf(self):
        r = self.requests.get(self.url).json()
        vnfs = {}
        for vnf in r["vnfs"]:
            vnfs[vnf["name"].encode("utf-8")] = vnf["id"].encode("utf-8")
        return vnfs

    def create_vnf(self, vnf_name, vnfd_id):
        values = {
            "vnf": {
                "name": vnf_name,
                "vnfd_id": vnfd_id
            }
        }
        data = json.dumps(values)
        r = self.requests.post(self.url, data)
        if "201" in str(r):
            print "The VNF:%s was created successfully!" % vnf_name
        else:
            print "Creating %s meets ERROR!" % vnf_name

    def show_vnf(self, vnf_name):
        vnf_list = self.list_vnf()
        vnf_id = vnf_list[vnf_name]
        url = self.url + "/" + vnf_id
        r = self.requests.get(url).json()
        json_r = json.dumps(r, sort_keys=True, indent=4, separators=(',',': '))
        print json_r


    def delete_vnf(self, vnf_name):
        vnf_list = self.list_vnf()
        vnf_id = vnf_list[vnf_name]
        url = self.url + "/" + vnf_id
        r = self.requests.delete(url)
        if "204" in str(r):
            print "The VNF:%s was deleted successfully!" % vnf_name
        elif "404" in str(r):
            print "%s was Not Found!" % vnf_name
        elif "401" in str(r):
            print "Your action was Unauthorized!"
        else:
            print "Other ERROR"


class vnfd(object):
    def __init__(self):
        self.url = "http://192.168.1.91:9890/v1.0/vnfds"
        self.requests = openstack_requests()

    def list_vnfd(self):
        r = self.requests.get(self.url).json()
        vnfds = {}
        for vnfd in r["vnfds"]:
            vnfds[vnfd["name"].encode("utf-8")] = vnfd["id"].encode("utf-8")
        return vnfds

    def create_vnfd(self, vnfd_file):
        f = open("vnfd/" + vnfd_file, 'r')
        r = self.requests.post(self.url, f)
        f.close()
        if "201" in str(r):
            vnfd_name = r.json()["vnfd"]["name"]
            print "The VNFD:%s was created successfully!" % vnfd_name
        elif "400" in str(r):
            print "Bad request: some content in the request was invalid."
        elif "401" in str(r):
            print "Unauthorized: user must authenticate before making a request."
        else:
            print "Internal Server Error."
        
    def show_vnfd(self, vnfd_name):
        vnfd_list = self.list_vnfd()
        vnfd_id = vnfd_list[vnfd_name]
        url = self.url + "/" + vnfd_id
        r = self.requests.get(url).json()
        json_r = json.dumps(r, sort_keys=True, indent=4, separators=(',',': '))
        print json_r

    def delete_vnfd(self, vnfd_name):
        vnfd_list = self.list_vnfd()
        vnfd_id = vnfd_list[vnfd_name]
        url = self.url + "/" + vnfd_id
        r = self.requests.delete(url)
        if "204" in str(r):
            print "The VNFD:%s was deleted successfully!" % vnfd_name
        elif "404" in str(r):
            print "%s was Not Found!" % vnfd_name
        elif "401" in str(r):
            print "Your action was Unauthorized!"
        else:
            print "Other ERROR"


class vnffg(object):
    def __init__(self):
        self.url = "http://192.168.1.91:9890/v1.0/vnffgs"
        self.requests = openstack_requests()

    def list_vnffg(self):
        r = self.requests.get(self.url).json()
        vnffgs = {}
        for vnffg in r["vnffgs"]:
            vnffgs[vnffg["name"].encode("utf-8")] = vnffg["id"].encode("utf-8")
        return vnffgs

    def create_vnffg(self, vnffg_name, vnffgd_id, vnf_mapping):
        values = {
            "vnffg": {
                "name": vnffg_name,
                "vnffgd_id": vnffgd_id,
                "vnf_mapping": vnf_mapping,
                "symmetrical": False 
            }
        }
        data = json.dumps(values)
        r = self.requests.post(self.url, data)
        if "201" in str(r):
            print "The VNFFG:%s was created successfully" % vnffg_name
        else:
            print "Creating %s meets ERROR!" % vnffg_name


    def show_vnffg(self, vnffg_name):
        vnffg_list = self.list_vnffg()
        vnffg_id = vnffg_list[vnffg_name]
        url = self.url + "/" + vnffg_id
        r = self.requests.get(url).json()
        json_r = json.dumps(r, sort_keys=True, indent=4, separators=(',',': '))
        print json_r

    def delete_vnffg(self, vnffg_name):
        vnffg_list = self.list_vnffg()
        vnffg_id = vnffg_list[vnffg_name]
        url = self.url + "/" + vnffg_id
        r = self.requests.delete(url)
        if "204" in str(r):
            print "The VNFFG:%s was deleted successfully!" % vnffg_name
        elif "404" in str(r):
            print "%s was Not Found!" % vnffg_name
        elif "401" in str(r):
            print "Your action was Unauthorized!"
        else:
            print "Other ERROR"


class vnffgd(object):
    def __init__(self):
        self.url = "http://192.168.1.91:9890/v1.0/vnffgds"
        self.requests = openstack_requests()

    def list_vnffgd(self):
        r = self.requests.get(self.url).json()
        vnffgds = {}
        for vnffgd in r["vnffgds"]:
            vnffgds[vnffgd["name"].encode("utf-8")] = vnffgd["id"].encode("utf-8")
        return vnffgds

    def create_vnffgd(self, vnffgd_file):
        f = open("vnffgd/" + vnffgd_file, 'r')
        r = self.requests.post(self.url, f)
        f.close()
        if "201" in str(r):
            vnffgd_name = r.json()["vnffgd"]["name"]
            print "The VNFFGD:%s was created successfully!" % vnffgd_name
        elif "400" in str(r):
            print "Bad request: some content in the request was invalid."
        elif "401" in str(r):
            print "Unauthorized: user must authenticate before making a request."
        else:
            print "Internal Server Error."
        
    def show_vnffgd(self, vnffgd_name):
        vnffgd_list = self.list_vnffgd()
        vnffgd_id = vnffgd_list[vnffgd_name]
        url = self.url + "/" + vnffgd_id
        r = self.requests.get(url).json()
        json_r = json.dumps(r, sort_keys=True, indent=4, separators=(',',': '))
        print json_r

    def delete_vnffgd(self, vnffgd_name):
        vnffgd_list = self.list_vnffgd()
        vnffgd_id = vnffgd_list[vnffgd_name]
        url = self.url + "/" + vnffgd_id
        r = self.requests.delete(url)
        if "204" in str(r):
            print "The VNFFGD:%s was deleted successfully!" % vnffgd_name
        elif "404" in str(r):
            print "%s was Not Found!" % vnffgd_name
        elif "401" in str(r):
            print "Your action was Unauthorized!"
        else:
            print "Other ERROR"

