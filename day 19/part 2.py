x = 0
y = 0
count = 0

with open("input.txt", "r") as file:
    contents = [x[:-1] for x in file.readlines()]
    field = [[x for x in y] for y in contents]
    x = field[0].index("|")

    running = True
    directions = [(0,-1), (1,0), (0,1), (-1 ,0)]
    direction = (0,1)
    word = ""
    while running:
        count += 1
        x += direction[0]
        y += direction[1]
        curr = field[y][x]
        if(curr in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            word += curr
        if(curr == "+"):
            oldD = direction
            for d in directions:
                x2 = x + d[0]
                y2 = y + d[1]
                try:
                    nxt = field[y2][x2]
                    if(nxt != " " and d != (-oldD[0], -oldD[1])):
                        # print(d, direction, (-direction[0], -direction[1]), (x, y))
                        direction = d
                except:
                    pass
            if(direction == oldD):
                print("Finished: ", count)
                break
        if(curr == " "):
            print("Finished: ",² count)
            break
        # print(curr)
