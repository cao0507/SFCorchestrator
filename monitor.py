
"""This module is a monitor of the cloud platform"""

from openstack_api import server


def server_status():
    """Get the relationship between servers' name and ip."""
    available_server = server().list_avaiable_server()
    data = json.dumps(available_server,
                      sort_keys=True, indent=4, separators=(',', ': '))
    f = open("status/available_server.json", 'w')
    f.write(data)
    f.close()


if __name__ == "__main__":
    while(True):
        server_status()
        sleep(5)