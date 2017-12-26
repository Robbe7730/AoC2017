positions = [x for x in range(16)]
translate = [x for x in "abcdefghijklmnopqrstuvwxyz"]
cycle = []

with open("input.txt", "r") as file:
    contents = file.readlines()[0].strip().split(",")
    for i in range(1000000000 % 60):
        print(i, "".join([translate[x] for x in positions]))
        if(positions in cycle):
            break
        else:
            cycle.append(positions[:])
        for step in contents:
            action = step[0]
            args = step[1:]
            if(action == "s"):
                newStart = len(positions) - int(float(args))
                positions = positions[newStart:] + positions[:newStart]
            if(action == "x"):
                args = args.split("/")
                a = int(float(args[0]))
                b = int(float(args[1]))
                memory = positions[a]
                positions[a] = positions[b]
                positions[b] = memory
            if(action == "p"):
                args = args.split("/")
                aText = args[0]
                bText = args[1]
                aNum = translate.index(aText)
                bNum = translate.index(bText)
                a = positions.index(aNum)
                b = positions.index(bNum)
                memory = positions[a]
                positions[a] = positions[b]
                positions[b] = memory
print("".join([translate[x] for x in positions]))
