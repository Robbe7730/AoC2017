with open ("input.txt", "r") as inputfile:
    firstChar = inputfile.read(1)
    char = firstChar
    count = 0
    while True:
        prevChar = char
        char = inputfile.read(1)
        if not char or char == "\n":
            break
        if(prevChar == char):
            count += float(char)
    if(firstChar == prevChar):
        count += float(prevChar)
    print(count)
