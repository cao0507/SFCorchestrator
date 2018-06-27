
"""This module will finish the whole SFC deployment operation"""

import os
import shutil

import create

import delete

from parse_request import jsonparser

import update


def deploy(template_sfc_file):
    """The function executes SFC deployment operation.

    :param template_sfc_file: the filename of sfc to be deployed
    """
    req = jsonparser(template_sfc_file)
    operation = req.get_sfc_operation()
    if operation == "create":
        sfc_file = req.get_sfc_name() + ".json"
        shutil.copyfile("sfc/"+template_sfc_file, "sfc/"+sfc_file)
        create.create(sfc_file)
    elif operation == "delete":
        sfc_file = req.get_sfc_name() + ".json"
        delete.delete(sfc_file)
        os.remove("sfc/" + sfc_file)
    else:
        sfc_file = req.get_sfc_name() + ".json"
        compare_output_file = compare_file(template_sfc_file, sfc_file)
        update.update(compare_output_file)

        
if __name__ == '__main__':
    deploy("template_sfc.json")
