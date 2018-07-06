
"""This module is a monitor of the cloud platform"""

import os
import sys
sys.path.append(r"/home/openstack/SFCorchestrator")

from api.openstack_api import server
import time
import json
import config


def server_status():
    """Get the relationship between servers' name and ip."""
    available_server = server().list_avaiable_server()
    data = json.dumps(available_server,
                      sort_keys=True, indent=4, separators=(',', ': '))
    file_path = config.abs_dir
    f = open(file_path + "/json/status/server_list.json", 'w')
    f.write(data)
    f.close()


if __name__ == "__main__":
    while(True):
        server_status()
        time.sleep(5)
