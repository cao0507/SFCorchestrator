import json
import requests

def get_token():
    url = "http://192.168.1.91/identity/v3/auth/tokens"
    values = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "id": "887d12795af74000ab618b1954429a3d",
                        "password": "openstack"
                    }
                }
            },
            "scope": {
                "project": {
                    "id": "3a7a49ccfef943ebae2457feabc2931e"
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
