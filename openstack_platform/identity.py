import json
import requests
import os
import sys
sys.path.append(r"/home/openstack/SFCorchestrator")
import config

def get_token():
    url = "http://" + config.service_ip + "/identity/v3/auth/tokens"
    file_path = os.path.dirname(__file__)
    if file_path is not '':
        file_path = file_path + "/"
    data = open(file_path + "auth.json", "r")
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
