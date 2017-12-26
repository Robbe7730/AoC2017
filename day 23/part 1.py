class CPU(object):
    def getValue(self, key):
        try:
            ret = int(key)
        except:
            ret = self.registers[key]
        return ret

    def __init__(self, instructions):
        self.count = 0
        self.instructions = [x.split(" ") for x in instructions]
        self.pointer = 0
        self.registers = {}
        for char in "abcdefgh":
            self.registers[char] = 0


    def doStep(self):
        instruction = self.instructions[self.pointer]
        print(self.pointer, self.instructions[self.pointer], self.getValue(instruction[1]), self.getValue(instruction[2]), self.count)
        if(instruction[0] == "set"):
            self.registers[instruction[1]] = self.getValue(instruction[2])
        if(instruction[0] == "add"):
            self.registers[instruction[1]] += self.getValue(instruction[2])
        if(instruction[0] == "sub"):
            self.registers[instruction[1]] -= self.getValue(instruction[2])
        if(instruction[0] == "mul"):
            self.count += 1
            self.registers[instruction[1]] *= self.getValue(instruction[2])
        if(instruction[0] == "jnz"):
            self.pointer += (self.getValue(instruction[2]) - 1) if self.getValue(instruction[1]) != 0 else 0
        self.pointer += 1

with open("input.txt", "r") as file:
    instructions = [x.strip() for x in file.readlines()]
    cpu = CPU(instructions)
    while True:
        cpu.doStep()
