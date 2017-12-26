with open("input.txt", "r") as file:
    line = file.readlines()[0].strip().split(",")
    north = line.count("n")
    south = line.count("s")
    northwest = line.count("nw")
    southwest = line.count("sw")
    northeast = line.count("ne")
    southeast = line.count("se")
    print(abs(north - south) + abs(northwest - southeast) + abs(northeast - southwest) - min(abs(northeast - southwest), abs(northwest - southeast)))
