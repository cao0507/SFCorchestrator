import tacker
import json
import configure_file
import time

f = open("vnfd/sfc1_vnf1_Description.json", 'r')
print type(f)
print f
data1 = json.load(f)

print type(data1)
print data1

data2 = json.dumps(f)
print type(data2)
print data2
f.close()

values = {
    "vnf": {
        "name": "vnf1",
        "vnfd_id": "1233435646"
    }
}
print type(values)
print values

data = json.dumps(values)
print type(data)
print data


