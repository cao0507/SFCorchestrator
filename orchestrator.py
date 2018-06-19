
"""
This module includes orchestration algorithms of SFC.
Any other orchestration alogrithm can be added here.
"""


def orchestrate(vnfs, cons):
    """A simple orchestration algorithm.

    Keyword arguments:
    vnfs -- the list of VNFs to be orchestrated
    cons -- the list of sequence constrains between two kinds of VNFs
    """
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

