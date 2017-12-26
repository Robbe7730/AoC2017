memory = []
for i in range(90):
    memory.append(0)

count = 0

def run(offset):
    for i in range(90):
        if(memory[i] != 0):
            if((i+offset)%((memory[i]-1)*2) == 0):
                return False
    # print("({}+{})%(({}-1)*2)".format(i,offset,memory[i]))
    return True

with open("input.txt", "r") as file:
    contents = file.readlines()
    contents = [x.strip() for x in contents]
    for line in contents:
        parsedline = line.split(": ")
        parsedline = [int(float(x)) for x in parsedline ]
        memory[parsedline[0]] = parsedline[1]
    for offset in range(100000000):
        if(run(offset)):
            print(offset)
