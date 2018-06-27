
"""
This module includes mapping algorithms of SFC.
Any other mapping algorithm can be add here.
"""


def sfc_mapper(sfc, hosts, objective):
    """A mapping algorithm of SFC.

    description:
    Construct the mapping relationship between
    virtual machines and physical hosts.
    
    Keyword arguments:
    sfc -- the list of SFs including flavor information
    hosts -- the list of hosts including available resource information
    objective -- the optimal objective of this mapping algorithm 
    """
    mapper_result = {}
    if objective == "bandwidth" or objective == "delay":
        cpu = 0
        memory = 0
        disk = 0
        for sf in sfc:
            cpu += sf["cpu"]
            memory += sf["memory"]
            disk += sf["disk"]
        available_hosts = []
        for host in hosts:
            if host["cpu"] >= cpu and\
               host["memory"] >= memory and\
               host["disk"] >= disk:
                available_hosts.append(host)
        if available_hosts:
            available_hosts_sorted_by_cpu = sorted(available_hosts, key=(lambda x: x["cpu"]), reverse=True)
            available_hosts_sorted_by_memory = sorted(available_hosts, key=(lambda x: x["memory"]), reverse=True)
            available_hosts_sorted_by_disk = sorted(available_hosts, key=(lambda x: x["disk"]), reverse=True)
            priority = {}
            for host in available_hosts:
                priority[host["name"]] = available_hosts_sorted_by_cpu.index(host) + available_hosts_sorted_by_memory.index(host) + available_hosts_sorted_by_disk.index(host)
            result = min(priority, key=priority.get)
            for sf in sfc:
                mapper_result[sf["name"].encode("utf-8")] = result.encode("utf-8")
        else:
            hosts_sorted_by_cpu = sorted(hosts, key=(lambda x: x["cpu"]), reverse=True)
            hosts_sorted_by_memory = sorted(hosts, key=(lambda x: x["memory"]), reverse=True)
            hosts_sorted_by_disk = sorted(hosts, key=(lambda x: x["disk"]), reverse=True)
            priority = {}
            for host in hosts:
                priority[host["name"]] = hosts_sorted_by_cpu.index(host) + hosts_sorted_by_memory.index(host) + hosts_sorted_by_disk.index(host)
            sorted_hosts = []
            for pri in sorted(priority.items(), key=(lambda x: x[1])):
                for host in hosts:
                    if host["name"] == pri[0]:
                        sorted_hosts.append(host)
            while sfc:
                sf = sfc.pop(0)
                while sorted_hosts:
                    if sorted_hosts[0]["cpu"] >= sf["cpu"] and sorted_hosts[0]["memory"] >= sf["memory"] and sorted_hosts[0]["disk"] >= host["disk"]:
                        sorted_hosts[0]["cpu"] -= sf["cpu"]
                        sorted_hosts[0]["memory"] -= sf["memory"]
                        sorted_hosts[0]["disk"] -= sf["disk"]
                        mapper_result[sf["name"].encode("utf-8")] = sorted_hosts[0]["name"].encode("utf-8")
                        break
                    else:
                        sorted_hosts.pop(0)
                if sorted_hosts:
                    pass
                else:
                    print ("Error! No available host")
                    return {}
    else:
        sorted_sfc = sorted(sfc, key=(lambda x: x[objective]))
        while sorted_sfc:
            sorted_hosts = sorted(hosts,
                                  key=(lambda x: x[objective]),
                                  reverse=True)
            sf = sorted_sfc.pop()
            for i in range(len(sorted_hosts)):
                if sorted_hosts[i]["cpu"] >= sf["cpu"] and \
                   sorted_hosts[i]["memory"] >= sf["memory"] and \
                   sorted_hosts[i]["disk"] >= sf["disk"]:
                    mapper_result[sf["name"].encode("utf-8")] = sorted_hosts[i]["name"].encode("utf-8")
                    sorted_hosts[i]["cpu"] -= sf["cpu"]
                    sorted_hosts[i]["memory"] -= sf["memory"]
                    sorted_hosts[i]["disk"] -= sf["disk"]
                    break
                elif i == len(sorted_hosts) - 1:
                    print ("Error! No available host")
                    return {}
    return mapper_result
