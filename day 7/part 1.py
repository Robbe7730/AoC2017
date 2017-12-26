tree = {}
weights = {}
parent = ''

with open("input.txt", "r") as file:
    content = file.readlines()
    for line in content:
        line = line.strip()
        data = line.split("->")
        parent = data[0].split(' ')[0]
        if("->" in line):
            children = data[1].strip().split(',')
            for child in children:
                tree[child] = parent
            print(tree)


def getParent(child):
    if(tree[child] == child):
        return child
    else:
        return getParent(tree[child])

print(getParent(parent))
