import json


class jsonparser(object):

    def __init__(self, filename):
        f = open(filename)
        self.req = json.load(f)
        f.close()

    def get_service_ip(self):
        return self.req["service_ip"]

    def get_user_id(self):
        return self.req["user_id"]

    def get_password(self):
        return self.req["password"]

    def get_tenant_id(self):
        return self.req["tenant_id"]

    def get_src_port_id(self):
        return self.req["src_port_id"]

    def get_dst_ip(self):
        return self.req["dst_ip"]
