
"""This module will finish the whole SFC deployment operation"""

import os
import shutil

from operation.create import create
from operation.delete import delete
#from operation.update import update

from parse_file.parse_request import jsonparser



def deploy(template_sfc_file):
    """The function executes SFC deployment operation.

    :param template_sfc_file: the filename of sfc to be deployed
    """
    req = jsonparser(template_sfc_file)
    operation = req.get_sfc_operation()
    sfc_name = req.get_sfc_name()
    if operation == "create":
        sfc_file = sfc_name + ".json"
        shutil.copyfile("json/sfc/"+template_sfc_file, "json/sfc/"+sfc_file)
        create(sfc_file)

    elif operation == "delete":
        sfc_file = sfc_name + ".json"
        delete(sfc_file)
        os.remove("json/sfc/" + sfc_file)
        for vnfd_description_file in os.listdir("json/vnfd/"):
            if sfc_name in vnfd_description_file:
                os.remove("json/vnfd/" + vnfd_description_file)
        for vnffgd_description_file in os.listdir("json/vnffgd/"):
            if sfc_name in vnffgd_description_file:
                os.remove("json/vnffgd/" + vnffgd_description_file)

    else:
        sfc_file = sfc_name + ".json"
        compare_output_file = compare_file(template_sfc_file, sfc_file)
        update(compare_output_file)

        
if __name__ == '__main__':
    deploy("template_sfc.json")
