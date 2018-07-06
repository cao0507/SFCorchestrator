import json
import requests
from config import abs_dir

import sys
sys.path.append(abs_dir)

from openstack_platform.identity import get_token

class api_request(object):
    def __init__(self):
        token = get_token()
        self.headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": token
        }

    def get(self, url):
        r = requests.get(url, headers=self.headers)
        return r

    def post(self, url, data):
        r = requests.post(url, data, headers=self.headers)
        return r

    def delete(self, url):
        r = requests.delete(url, headers=self.headers)
        return r
