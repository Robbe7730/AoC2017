memory = []
count = 0

with open("input.txt", "r") as file:
    line = file.readlines()[0].strip();
    linelist = line.split('\t')
    linelist = [int(float(x)) for x in linelist]
    while linelist not in memory:
        memory.append(linelist[:])
        maxidx = linelist.index(max(linelist))
        # print(linelist)
        # print(maxidx)
        count += 1
        value = linelist[maxidx]
        linelist[maxidx] = 0
        for i in range(value):
            linelist[(maxidx+i+1)%len(linelist)] += 1
            # print((maxidx+i)%len(linelist))
        # print(linelist)
        # print(memory)
        # a = input("")
print(count)
