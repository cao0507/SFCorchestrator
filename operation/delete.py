
"""
This module is used to delete an existed SFC
according to request json file.
"""

import time

from parse_file.parse_request import jsonparser

import api.tacker_api as tacker


def delete(sfc_file):
    """The function executes SFC delete action.

    :param sfc_file: the filename of SFC to be deleted
    """
    tacker_vnf = tacker.vnf()
    tacker_vnfd = tacker.vnfd()
    tacker_vnffg = tacker.vnffg()
    tacker_vnffgd = tacker.vnffgd()
    req = jsonparser(sfc_file)

    sfc_name = req.get_sfc_name()
    
    # list all the component of the sfc

    vnf_name_list = tacker_vnf.list_vnf().keys()
    vnfd_name_list = tacker_vnfd.list_vnfd().keys()
    vnffg_name_list = tacker_vnffg.list_vnffg().keys()
    vnffgd_name_list = tacker_vnffgd.list_vnffgd().keys()
    
    # delete vnffg
    for vnffg_name in vnffg_name_list:
        if sfc_name in vnffg_name:
            tacker_vnffg.delete_vnffg(vnffg_name)
            time.sleep(10)
  
    # delete vnfs
    for vnf_name in vnf_name_list:
        if sfc_name in vnf_name:
            tacker_vnf.delete_vnf(vnf_name)
            time.sleep(10)

    # delete vnfds
    for vnfd_name in vnfd_name_list:
        if sfc_name in vnfd_name:
            tacker_vnfd.delete_vnfd(vnfd_name)
            time.sleep(2)

    # delete vnffgd
    for vnffgd_name in vnffgd_name_list:
        if sfc_name in vnffgd_name:
            tacker_vnffgd.delete_vnffgd(vnffgd_name)
            time.sleep(2)


if __name__ == "__main__":
    delete("sfc1.json")
