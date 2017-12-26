cursor = 0
count = 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [int(float(x.strip())) for x in lines]
    while ((cursor >= 0) and (cursor < len(lines))):
        if(lines[cursor] >= 3):
            lines[cursor] -= 1
            cursor += lines[cursor] + 1
        else:
            lines[cursor] += 1
            cursor += lines[cursor] - 1
        count += 1
        # print(lines)
        # print(cursor)
print(count)
