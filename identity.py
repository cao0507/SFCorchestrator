import json
import requests

def get_token():
    url = "http://192.168.1.30/identity/v3/auth/tokens"
    values = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "id": "ad51db7366fd49e29545602172da7747",
                        "password": "openstack"
                    }
                }
            },
            "scope": {
                "project": {
                    "id": "884a98138b784608bdbb03ff3cb958fa"
                }
            }
        }
    }
    data = json.dumps(values)
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }
    r = requests.post(url, data, headers=headers)
    token = r.headers.get('X-Subject-Token')
    return token

if __name__ == '__main__':
    token = get_token()
    print (token)
