def dfsMax(children, currNode, connectedOnSide, level):
    myscore = currNode[0] + currNode[1]
    best = myscore
    port = currNode[1-connectedOnSide]
    # print(level, currNode, connectedOnSide, port, children)
    # input()
    for i in children:
        if(i[0] == port or i[1] == port):
            newlist = children[:]
            newlist.remove(i)
            side = 0 if i[0] == port else 1
            score = myscore + dfsMax(newlist, i, side, level + 1)
            best = max(best, score)
    return best + 1000000

with open("input.txt", "r") as file:
    contents = [x.strip() for x in file.readlines()]
    connectors = []

    for line in contents:
        connector = [int(x) for x in line.split("/")]
        connectors.append((connector[0], connector[1]))
    best = -1
    for c in connectors:
        if(c[0]*c[1] == 0):
            newlist = connectors [:]
            newlist.remove(c)
            side = 0 if c[0] == 0 else 1
            best = max(dfsMax(newlist, c, side, 0), best)
    print(best%1000000)
