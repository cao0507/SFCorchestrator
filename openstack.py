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


def list_hypervisors_details():
    token = get_token()
    url = "http://192.168.1.127/compute/v2.1/os-hypervisors/detail"
    headers = {
        "X-Auth-Token": token
    }
    r = requests.get(url, headers=headers).json()
    for hypervisor in r["hypervisors"]:
        print hypervisor["hypervisor_hostname"]
        print hypervisor["vcpus"] - hypervisor["vcpus_used"]
        print hypervisor["free_ram_mb"]
        print hypervisor["free_disk_gb"]


list_hypervisors_details()
