class State(object):
    def __init__(self, action0, action1):
        self.action0 = action0
        self.action1 = action1

    def run(self, tape, pointer):
        if tape[pointer] == 0:
            tape[pointer] = self.action0[0]
            pointer += self.action0[1]
            newState = self.action0[2]
        else:
            tape[pointer] = self.action1[0]
            pointer += self.action1[1]
            newState = self.action1[2]
        return (tape, pointer, newState)

states = {
    "A": State((1,1,"B"), (0, -1, "B")),
    "B": State((1,-1,"C"), (0, 1, "E")),
    "C": State((1,1,"E"), (0, -1, "D")),
    "D": State((1,-1,"A"), (1, -1, "A")),
    "E": State((0,1,"A"), (0, 1, "F")),
    "F": State((1,1,"E"), (1, 1, "A"))
}

stateLetter = "A"
tape = [0 for i in range(100000)]
pointer = 50000
for i in range(12861455):
    tape, pointer, stateLetter = states[stateLetter].run(tape, pointer)
    # print(pointer, stateLetter)
    if (pointer < 0):
        print(pointer)
print(tape.count(1))
