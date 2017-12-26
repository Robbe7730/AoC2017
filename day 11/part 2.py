position = {}
position["north"] = 0
position["northwest"] = 0
position["northeast"] = 0
position["south"] = 0
position["southwest"] = 0
position["southeast"] = 0
maximum = 0

with open("input.txt", "r") as file:
    line = file.readlines()[0].strip().split(",")
    for direction in line:
        if(direction == "n"):
            position["north"] += 1

        if(direction == "s"):
            position["south"] += 1

        if(direction == "nw"):
            position["northwest"] += 1

        if(direction == "sw"):
            position["southwest"] += 1

        if(direction == "ne"):
            position["northeast"] += 1

        if(direction == "se"):
            position["southeast"] += 1

        maximum = max(maximum,abs(position["north"] - position["south"]) + abs(position["northwest"]-position["southeast"]) + abs(position["northeast"]-position["southwest"]) - min(abs(position["northeast"]-position["southwest"]), abs(position["northwest"]-position["southeast"])))

print(maximum)
