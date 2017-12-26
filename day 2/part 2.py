with open("input.txt", "r") as file:
    content = file.readlines()
    content = [x.strip() for x in content]

sum = 0
for line in content:
    values = line.split("\t")
    values = [float(value) for value in values]
    for value in values:
        for testValue in values:
            if((value%testValue == 0) and value != testValue):
                sum += value/testValue
print(sum)
