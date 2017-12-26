children = {}
weights = {}
parent = ''

def getweight(program):
    if(program in children):
        som = weights[program]
        for child in children[program]:
            som += getweight(child)
            # print(child)
        return som
    else:
        return weights[program]

with open("input.txt", "r") as file:
    content = file.readlines()
    for line in content:
        line = line.strip()
        data = line.split("->")
        parent = data[0].split(' ')[0]
        weights[parent] = float(data[0].split(' ')[1][1:-1])
        # print(weights[parent])
        if("->" in line):
            childrn = data[1].strip().split(',')
            children[parent] = [x.strip() for x in childrn]
    for parent in children:
        weightsP = {}
        for child in children[parent]:
            print("\t {}: {}".format(child, weights[child]))
            weightsP[child] = getweight(child)
        allweights = set([weightsP[x] for x in weightsP])
        if(len(allweights) > 1):
            print(parent)
            print(weightsP)
