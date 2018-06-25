from tacker import vnf,vnfd,vnffg,vnffgd

aa = vnf()
bb = vnfd()
cc = vnffg()
dd = vnffgd()

vnfs = aa.list_vnf()
vnfds = bb.list_vnfd()
vnffgs = cc.list_vnffg()
vnffgds = dd.list_vnffgd()

print "****************The VNFs list.****************"
print vnfs
print "\n****************The VNFDs list.****************"
print vnfds
print "\n****************The VNFFGs list.****************"
print vnffgs
print "\n****************The VNFFGDs list.****************"
print vnffgds
print "\n====================================================================\n"

vnf1_name = "vnf1"
vnf2_name = "vnf2"
vnfd1_name = "VNFD1"
vnfd2_name = "VNFD2"
vnfd1_file = "vnfd1.json"
vnfd2_file = "vnfd2.json"
vnffgd_file = "vnffgd.json"
vnffg_name = "vnffg"
vnffgd_name = "VNFFGD"


#aa.delete_vnf(vnf1_name)
#aa.delete_vnf(vnf2_name)

#bb.delete_vnfd(vnfd1_name)
#bb.delete_vnfd(vnfd2_name)
#
#cc.delete_vnffg(vnffg_name)
#
#dd.delete_vnffgd(vnffgd_name)

#aa.show_vnf("vnf1")
#bb.show_vnfd("VNFD1")
#cc.show_vnffg("vnffg")
#dd.show_vnffgd("vnffgd-test")


#bb.create_vnfd(vnfd1_file)
#bb.create_vnfd(vnfd2_file)
#
#
#aa.create_vnf(vnf1_name, vnfd1_name)
#aa.create_vnf(vnf2_name, vnfd2_name)
#
#

#dd.create_vnffgd(vnffgd_file)


#vnf1_id = vnfs[vnf1_name]
#vnf2_id = vnfs[vnf2_name]
#vnf_mapping = {
#    vnfd1_name: vnf1_id,
#    vnfd2_name: vnf2_id
#}
#cc.create_vnffg(vnffg_name, vnffgd_name, vnf_mapping)

vnfs = aa.list_vnf()
vnfds = bb.list_vnfd()
vnffgs = cc.list_vnffg()
vnffgds = dd.list_vnffgd()

print "\n====================================================================\n"
print "****************The VNFs list.****************"
print vnfs
print "\n****************The VNFDs list.****************"
print vnfds
print "\n****************The VNFFGs list.****************"
print vnffgs
print "\n****************The VNFFGDs list.****************"
print vnffgds
