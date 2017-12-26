count = 0;

x = 1
y = 0
direction = 1
level = 1
curr = 2

while curr != 347991:
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

    curr += 1
    print("{:d}: {:d}, {:d}, direction: {:d}".format(curr, x, y, direction))


print(abs(x) + abs(y))
