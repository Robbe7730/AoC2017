memory = []
for i in range(100):
    memory.append(0)

count = 0

with open("input.txt", "r") as file:
    contents = file.readlines()
    contents = [x.strip() for x in contents]
    for line in contents:
        parsedline = line.split(": ")
        parsedline = [int(float(x)) for x in parsedline ]
        memory[parsedline[0]] = parsedline[1]
    for i in range(90):
        if(memory[i] != 0):
            if(i%((memory[i]-1)*2) == 0):
                count += memory[i]*i
                # print("{}%(({}-1)*2)".format(i, memory[i]))
print(count)
