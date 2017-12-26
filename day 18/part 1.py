lastTone = 0
recovered = 0
cursor = 0
memory = {}

def getFromMemory(key):
    try:
        ret = memory[key]
    except:
        try:
            ret = int(key)
        except:
            memory[key] = 0
            ret = int(memory[key])
    return ret

with open("input.txt", "r") as file:
    contents = [x.strip() for x in file.readlines()]

    while recovered == 0:
        a = contents[cursor].split(" ")
        arg = a[0]
        print(cursor, contents[cursor], memory)
        if(arg == "snd"):
            lastTone = getFromMemory(a[1])
        if(arg == "set"):
            memory[a[1]] = getFromMemory(a[2])
        if(arg == "add"):
            memory[a[1]] = int(getFromMemory(a[1])) + int(getFromMemory(a[2]))
        if(arg == "mul"):
            memory[a[1]] = int(getFromMemory(a[1])) * int(getFromMemory(a[2]))
        if(arg == "mod"):
            memory[a[1]] = int(getFromMemory(a[1])) % int(getFromMemory(a[2]))
        if(arg == "rcv"):
            recovered = lastTone
        if(arg == "jgz"):
            cursor += (int(getFromMemory(a[2])) - 1) if int(getFromMemory(a[1])) > 0 else 0
        cursor += 1
        # input()
    print(recovered)
