import re

with open("input.txt", "r") as file:
    line = file.readlines()[0]
    line = re.sub("!.", "", line)
    # print(line)
    line = re.sub("<[^>]*>", "", line)
    # print(line)
    line = re.sub(",", "", line)
    level = 0
    total = 0
    for char in line:
        if(char == "{"):
            level += 1
            total += level
        else:
            level -= 1
    # print(line)
    print(total)
