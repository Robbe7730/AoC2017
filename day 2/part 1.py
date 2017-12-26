with open("input.txt", "r") as file:
    content = file.readlines()
    content = [x.strip() for x in content]

sum = 0
for line in content:
    values = line.split("\t")
    min = 10000
    max = 0
    for value in values:
        fValue = float(value)
        if(fValue > max):
            max = fValue
        if(fValue < min):
            min = fValue
    sum += (max-min)
print(sum)
