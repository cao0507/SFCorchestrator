import json
import requests


def get_token():
    url = "http://192.168.1.127/identity/v3/auth/tokens"
    values = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "name": "Default"
                        },
                        "password": "openstack"
                    }
                }
            },
            "scope": {
                "domain": {
                    "name": "Default"
                }
            }
        }
    }
    data = json.dumps(values)
    r = requests.post(url, data)
    token = r.headers.get('X-Subject-Token')
    return token


def list_images():
    token = get_token()
    url = "http://192.168.1.127/image/v2/images"
    headers = {
        "X-Auth-Token": token
    }
    r = requests.get(url, headers=headers)
    images = []
    for image in r.json()["images"]:
        images.append(image["name"])
    print images
    # f = open("/home/openstack/data.txt", "w")
    # f.write(str(images))
    # f.close()

list_images()
