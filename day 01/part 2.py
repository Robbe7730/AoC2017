with open ("input.txt", "r") as testfile:
    content = testfile.readlines()

line = content[0]
length = len(line) - 1
count = 0

for i in range(length):
    if(line[i] == line[int(i + (length/2))%length]):
        count += float(line[i])µ

print(count)
