def knotHash(value):
    circle = []
    skipsize = 0
    cursor = 0

    for i in range(256):
        circle.append(i)
    lengths = [ord(x) for x in value] + [17,31,73,47,23]
    for mqslfkjsmlqdkjfmlsk in range(64):
        for l in lengths:
            newcircle = circle[:]
            for i in range(l):
                newcircle[(cursor+i)%len(circle)] = circle[(cursor+l-i-1)%len(circle)]
            circle = newcircle
            cursor += l + skipsize
            skipsize += 1
    ret = []
    for i in range(16):
        ret.append(circle[i*16])
        for j in range(15):
            ret[i] = ret[i] ^ circle[i*16+j+1]
    return("".join([("0" + hex(x)[2:] if len(hex(x)) == 3 else hex(x)[2:]) for x in ret]))
total = 0
for i in range(128):
    currentstr = "ffayrhll-{}".format(i)
    knot = knotHash(currentstr)
    binary = bin(int(knot, 16))[2:].zfill(128)
    total += binary.count("1")
print(total)
