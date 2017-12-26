import re

with open("input.txt", "r") as file:
    line = file.readlines()[0]
    line = re.sub("!.", "", line)
    # print(line)
    line = re.sub("<([^>]*)>", r"µ\1£", line)
    line = "£" + line + "µ"
    # print(line)
    line = re.sub("£([^µ]*)µ", "", line)
    # print(line)
    print(len(line))
