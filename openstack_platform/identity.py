import json
import requests
import os
import sys
sys.path.append(r"/home/openstack/SFCorchestrator")
import config

def get_token():
    url = "http://" + config.service_ip + "/identity/v3/auth/tokens"
    file_path = config.abs_dir
    data = open(file_path + "openstack_platform/auth.json", "r")
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }
    r = requests.post(url, data, headers=headers)
    data.close()
    token = r.headers.get('X-Subject-Token')
    return token

if __name__ == '__main__':
    token = get_token()
    print (token)
