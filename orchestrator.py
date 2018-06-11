def orchestrate(vnfs, cons):
    sfc = []
    for vnf in vnfs:
        if vnf not in sfc:
            sfc.append(vnf)
            for i in range(len(cons)):
                if vnf == cons[i][0]:
                    counter = 0
                    while cons[i][1] in sfc:
                        sfc.remove(cons[i][1])
                        counter += 1
                    for j in range(counter):
                        sfc.append(cons[i][1])
        else:
            for k in range(len(sfc)):
                if sfc[k] == vnf:
                    sfc.insert(k, vnf)
                    break
    return sfc

