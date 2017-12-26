count = 0;
with open("input.txt", "r") as file:
    contents = file.readlines()
    for line in contents:
        line = line.strip()
        values = line.split(" ")
        # print(values)
        if(len(values) == len(set(values))):
            count+=1
print(count)
