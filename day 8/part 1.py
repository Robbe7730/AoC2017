memory = {}

with open("input.txt", "r") as file:
    for line in file.readlines():
        contents = line.split(" ")
        if(contents[0] not in memory):
            memory[contents[0]] = 0
        if(contents[4] not in memory):
            memory[contents[4]] = 0
        increase = 1 if contents[1] == "inc" else -1
        if(contents[5] == "<"):
            filled = memory[contents[4]] < float(contents[6])
        if(contents[5] == "<="):
            filled = memory[contents[4]] <= float(contents[6])
        if(contents[5] == ">"):
            filled = memory[contents[4]] > float(contents[6])
        if(contents[5] == ">="):
            filled = memory[contents[4]] >= float(contents[6])
        if(contents[5] == "=="):
            filled = memory[contents[4]] == float(contents[6])
        if(contents[5] == "!="):
            filled = memory[contents[4]] != float(contents[6])
        if(filled):
            print("filled {}".format(line))
            memory[contents[0]] = memory[contents[0]] + increase * float(contents[2])

print(memory)
print(max([memory[x] for x in memory]))
