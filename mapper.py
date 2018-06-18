def sfc_mapper(sfc, hosts, target):
    mapper_result = {}
    if target == "bandwidth" or target == "delay":
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
                mapper_result[sf["name"]] = result
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
                        mapper_result[sf["name"]] = sorted_hosts[0]["name"]
                        break
                    else:
                        sorted_hosts.pop(0)
                if sorted_hosts:
                    pass
                else:
                    print ("Error! No available host")
                    return {}
    else:
        sorted_sfc = sorted(sfc, key=(lambda x: x[target]))
        while sorted_sfc:
            sorted_hosts = sorted(hosts,
                                  key=(lambda x: x[target]),
                                  reverse=True)
            sf = sorted_sfc.pop()
            for i in range(len(sorted_hosts)):
                if sorted_hosts[i]["cpu"] >= sf["cpu"] and \
                   sorted_hosts[i]["memory"] >= sf["memory"] and \
                   sorted_hosts[i]["disk"] >= sf["disk"]:
                    mapper_result[sf["name"]] = sorted_hosts[i]["name"]
                    sorted_hosts[i]["cpu"] -= sf["cpu"]
                    sorted_hosts[i]["memory"] -= sf["memory"]
                    sorted_hosts[i]["disk"] -= sf["disk"]
                    break
                elif i == len(sorted_hosts) - 1:
                    print ("Error! No available host")
                    return {}
    return mapper_result
