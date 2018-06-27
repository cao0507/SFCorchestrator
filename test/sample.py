import libvirt
conn = libvirt.open("qemu:///system")
for id in conn.listDomainsID():
    domain = conn.lookupByID(id)
    print domain.name()  
    print domain.UUIDString()
    print domain.info()
conn.close()