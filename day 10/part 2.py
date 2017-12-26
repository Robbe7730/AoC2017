circle = []
skipsize = 0
cursor = 0

for i in range(256):
    circle.append(i)

with open("input.txt", "r") as file:
    lengths = file.readlines()[0].strip()
    lengths = [ord(x) for x in lengths] + [17,31,73,47,23]
    for mqslfkjsmlqdkjfmlsk in range(64):
        for l in lengths:
            newcircle = circle[:]
            for i in range(l):
                # print("{} => {}".format(cursor+i, circle[(cursor+l-i-1)%len(circle)]))
                newcircle[(cursor+i)%len(circle)] = circle[(cursor+l-i-1)%len(circle)]
            circle = newcircle
            cursor += l + skipsize
            skipsize += 1
    print(circle)
    ret = []
    for i in range(16):
        ret.append(circle[i*16])
        for j in range(15):
            print(i*16+j+1)
            ret[i] = ret[i] ^ circle[i*16+j+1]
print("".join([hex(x)[2:] for x in ret]))
