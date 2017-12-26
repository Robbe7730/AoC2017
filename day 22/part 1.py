class Antivirus(object):
    padding = 500
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    def __init__(self, field):
        paddedField = []
        for i in range(self.padding):
            paddedField.append(["." for x in range(2*self.padding + len(field))])
        for line in field:
            newLine = ["." for x in range(self.padding)]
            newLine.extend(line)
            newLine.extend(["." for x in range(self.padding)])
            paddedField.append(newLine)
        for i in range(self.padding):
            paddedField.append(["." for x in range(2*self.padding + len(field))])
        # for line in paddedField:
        #     print("".join(line))
        self.count = 0
        self.field = paddedField
        self.pos = (int(len(self.field)/2), int(len(self.field)/2))
        self.direction = 0

    def step(self):
        x, y = self.pos
        if(self.field[x][y] == "."):
            self.count += 1
            self.field[x][y] = "#"
            self.direction = (self.direction - 1)%4

        elif(self.field[x][y] == "#"):
            self.field[x][y] = "."
            self.direction = (self.direction + 1)%4
        # for idx, line in enumerate(self.field):
        #     print(idx, "\t", "".join(line))
        # print(self.pos, self.direction, self.directions[self.direction])
        # input()

        dx, dy = self.directions[self.direction]
        self.pos = (x + dx, y + dy)

with open("input.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]
    field = []
    for line in lines:
        field.append([x for x in line])
    av = Antivirus(field)
    for i in range(10000):
        av.step()
    print(av.count)
