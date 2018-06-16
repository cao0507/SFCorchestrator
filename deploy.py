import json
import os
import shutil
from parse_request import jsonparser
import create,delete,update

def deploy(template_sfc_file):
    req = jsonparser(template_sfc_file)
    operation = req.get_sfc_operation()
    if operation == "create":
        sfc_file = req.get_sfc_name+".json"
        shutil.copyfile("sfc/"+template_sfc_file, "sfc/"+sfc_file)
        create(sfc_file)
    elif operation == "delete":
        sfc_file = req.get_sfc_name + ".json"
        delete(sfc_file)
        os.remove("sfc/" + sfc_file_name)
    else:
        sfc_file = req.get_sfc_name + ".json"
        compare_output_file = compare_file(template_sfc_file,sfc_file)
        update(compare_output_file)

if __name__ == '__main__':
    deploy("template_sfc")
