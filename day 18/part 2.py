import collections

class CPU(object):
    _id = 0
    instructions = []
    pointer = 0
    outQueue = []
    queue = []
    count = 0

    def getValue(self, key):
        try:
            ret = int(key)
        except:
            ret = self.registers[key]
        return ret

    def __init__(self, _id, instructions):
        self._id = _id;
        self.instructions = instructions;
        self.registers = collections.defaultdict(int)
        self.registers["p"] = _id
        self._id = 0
        self.pointer = 0
        self.outQueue = []
        self.queue = []
        self.count = 0

    def doStep(self, instruction):
        print(instruction, self.registers)
        if(instruction[0] == "set"):
            self.registers[instruction[1]] = self.getValue(instruction[2])
        if(instruction[0] == "add"):
            self.registers[instruction[1]] += self.getValue(instruction[2])
        if(instruction[0] == "mul"):
            self.registers[instruction[1]] *= self.getValue(instruction[2])
        if(instruction[0] == "mod"):
            self.registers[instruction[1]] %= self.getValue(instruction[2])
        if(instruction[0] == "snd"):
            self.count += 1
            self.outQueue.append(self.getValue(instruction[1]))
        if(instruction[0] == "rcv"):
            if(self.queue == []):
                return True
            self.registers[instruction[1]] = self.queue.pop(0)
        if(instruction[0] == "jgz"):
            self.pointer += (self.getValue(instruction[2]) - 1) if self.getValue(instruction[1]) > 0 else 0
        self.pointer += 1
        return False

    def doStepsUntilEmpty(self, inQueue):
        print("in ", self._id)
        self.queue = inQueue
        self.outQueue = []
        isWaiting = False
        while not isWaiting:
            instruction = self.instructions[self.pointer].split(" ")
            isWaiting = self.doStep(instruction)
        return self.outQueue

def do_things(instructions):
    a = CPU(0, instructions)
    b = CPU(1, instructions)

    didSomething = True
    retB = []
    while didSomething:
        retA = a.doStepsUntilEmpty(retB)
        if(retA == []):
            didSomething = False
        retB = b.doStepsUntilEmpty(retA)
        if(retB == []):
            didSomething = False
    print(b.count)
with open("input.txt", "r") as file:
    instructions = [x.strip() for x in file.readlines()]
    do_things(instructions)
