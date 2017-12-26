step_size = 366

memory = []
pos = 0

for i in range(2018):
    pos = (pos + step_size)%(len(memory))+1 if i != 0 else 0
    memory.insert(pos, i)
print(memory, pos, i, memory[pos + 1])
