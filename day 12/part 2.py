connected = []

for i in range(2000):
    connected.append([])
    for j in range(2000):
        connected[i].append(False)

with open("input.txt", "r") as file:
    contents = file.readlines()
    for line in contents:
        linesplit = line.split(" <-> ")
        parent = int(float(linesplit[0]))
        children = linesplit[1].split(",")
        children = [int(float(x.strip())) for x in children]
        for child in children:
            connected[parent][child] = True

rootNodes = []

for i in range(2000):
    rootNodes.append(i)

def iterateChildren(node, visited, root):
    print(visited)
    visited.append(node)
    rootNodes[node] = root
    count = 1
    for i in range(2000):
        if(connected[i][node] and (i not in visited)):
            iterateChildren(i, visited, root)

for i in range(2000):
    if(rootNodes[i] == i):
        iterateChildren(i, [], i)

print(len(set(rootNodes)))
