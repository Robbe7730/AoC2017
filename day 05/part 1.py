cursor = 0
count = 0
with open("sampleinput.txt", "r") as file:
    lines = file.readlines()
    lines = [int(float(x.strip())) for x in lines]
    while ((cursor >= 0) and (cursor < len(lines))):
        lines[cursor] += 1
        cursor += lines[cursor] - 1
        if(lines[cursor] >= 3):
            count -= 1
        else:
            count += 1
        print(lines)
        print(cursor)
print(count)
