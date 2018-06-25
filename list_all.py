
"""
This module is used to list all information of
VNFs, VNFDs, VNFFGs and VNFFGDs.
"""

import tacker


def list_all():
    """The function list all information currently."""
    tacker_vnf = tacker.vnf()
    tacker_vnfd = tacker.vnfd()
    tacker_vnffg = tacker.vnffg()
    tacker_vnffgd = tacker.vnffgd()

    print "\n**************The VNFs list.****************"
    print tacker_vnf.list_vnf()
    print "\n**************The VNFDs list.****************"
    print tacker_vnfd.list_vnfd()
    print "\n**************The VNFFGs list.****************"
    print tacker_vnffg.list_vnffg()
    print "\n**************The VNFFGDs list.****************"
    print tacker_vnffgd.list_vnffgd()
    print "\n===================================================================="
    print "====================================================================\n"

if __name__ == "__main__":
    list_all()
