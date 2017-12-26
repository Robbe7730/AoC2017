import math

class Convert(object):
    gotten = []
    def __init__(self, inRule, outRule):
        self.inRule = inRule.split("/")
        self.outRule = outRule.split("/")
        self.binHashes = []
        self.calculateHashes()

    def getSize(self):
        return len(self.inRule[0])

    def calculateHashes(self):
        curr = self.inRule[:]
        for i in range(4):
            self.binHashes.append(self.calculateHash(curr)) # normal
            self.binHashes.append(self.calculateHash([x[::-1] for x in curr])) # flipped
            curr = ["".join(x) for x in zip(*curr[::-1])] # rotate 90°

    def calculateHash(self, square):
        # print(square)
        binary = "".join(square).replace(".", "0").replace("#", "1")
        return int(binary, 2)

    def transform(self, field):
        # print(self.calculateHash(field.field))
        if(self.calculateHash(field) in self.binHashes):
            return self.outRule
        return field

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)

def splitIntoSquares(field):
    newField = []

    if(len(field[0])%2 == 0):
        for idx,(row1, row2) in enumerate(grouped(field, 2)):
            newField.append([])
            for i in range(0, len(row1), 2):
                newField[idx].append(["".join(row1[i:i+2]), "".join(row2[i:i+2])])
    elif(len(field[0])%3 == 0):
        for idx,(row1, row2, row3) in enumerate(grouped(field, 3)):
            newField.append([])
            for i in range(0, len(row1), 3):
                newField[idx].append(["".join(row1[i:i+3]), "".join(row2[i:i+3]), "".join(row3[i:i+3])])

    return newField

def join(field):
    allstring = ""
    ret = []
    for row in field:
        for i in range(len(row[0])):
            for square in row:
                allstring += square[i]
    a = int(math.sqrt(len(allstring)))
    for i in range(a):
        ret.append(allstring[i*a:i*a+a])
    return ret

def convert(field, converters, newMap):
    myMap = newMap[:]
    for converter in converters[len(field)]:
        fieldNew = converter.transform(field)
        if (fieldNew != field):
            myMap[idx].append(fieldNew)
            return myMap

with open("input.txt", "r") as file:
    rules = [x.strip().split(" => ") for x in file.readlines()]
    converters = [[] for i in range(4)]
    for rule in rules:
        c = Convert(rule[0], rule[1])
        converters[c.getSize()].append(c)

    fullMap = [".#.", "..#", "###"]
    for i in range(5):
        print("fullMap:", fullMap)
        fields = splitIntoSquares(fullMap)
        print("fields:", fields)
        newMap = []
        for idx, row in enumerate(fields):
            newMap.append([])
            for field in row:
                newMap = convert(field, converters, newMap)
        print("newMap:")
        for row in newMap:
            for square in row:
                print(square)
        fullMap = join(newMap)
        print("join(newMap):")
        for line in fullMap:
            print(line)
        input()
    count = 0
    for row in fullMap:
        count += row.count("#")
    print(count)
