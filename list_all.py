
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
    for vnf in tacker_vnf.list_vnf():
        print vnf
    print "\n**************The VNFDs list.****************"
    for vnfd in tacker_vnfd.list_vnfd():
        print vnfd
    print "\n**************The VNFFGs list.****************"
    for vnffg in tacker_vnffg.list_vnffg():
        print vnffg
    print "\n**************The VNFFGDs list.****************"
    for vnffgd in tacker_vnffgd.list_vnffgd():
        print vnffgd
    print "\n===================================================================="
    print "====================================================================\n"

if __name__ == "__main__":
    list_all()
