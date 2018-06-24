import json
import requests
import parse_platform

service_ip = "192.168.1.30" 

def get_token():
    url = "http://" + service_ip + "/identity/v3/auth/tokens"
    data = open("auth.json", "r")
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
