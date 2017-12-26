circle = []
skipsize = 0
cursor = 0

for i in range(256):
    circle.append(i)

with open("input.txt", "r") as file:
    lengths = file.readlines()[0].strip().split(",")
    lengths = [int(float(x)) for x in lengths]
    for l in lengths:
        newcircle = circle[:]
        for i in range(l):
            # print("{} => {}".format(cursor+i, circle[(cursor+l-i-1)%len(circle)]))
            newcircle[(cursor+i)%len(circle)] = circle[(cursor+l-i-1)%len(circle)]
        circle = newcircle
        cursor += l + skipsize
        skipsize += 1
print(circle)
