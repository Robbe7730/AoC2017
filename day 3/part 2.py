count = 0;

offset = 10

memory = [[0 for x in range(2*offset)] for y in range(2*offset)]

x = 1
y = 0
direction = 1
level = 1
curr = 2
memory[offset][offset] = 1
memory[offset+1][offset] = 1

while level < 5:
    if(direction == 0):
        if(x == level):
            direction = 1
        else:
            x += 1


    if(direction == 1):
        if(y == level):
            direction = 2
        else:
            y += 1

    if(direction == 2):
        if(x == -level):
            direction = 3
        else:
            x -= 1

    if(direction == 3):
        if(y == -level):
            direction = 0
            x += 1
            level += 1
        else:
            y -= 1

    memory[x + offset][y + offset] = memory[x+1 + offset][y + offset] + memory[x+1 + offset][y+1 + offset] + memory[x+1 + offset][y-1 + offset] + memory[x + offset][y+1 + offset] + memory[x + offset][y-1 + offset] + memory[x-1 + offset][y + offset] + memory[x-1 + offset][y+1 + offset] + memory[x-1 + offset][y-1 + offset]
    print("{:d}: {:d}, {:d}, direction: {:d}".format(memory[x + offset][y + offset], x, y, direction))


print(abs(x) + abs(y))
