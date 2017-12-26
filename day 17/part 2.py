step_size = 366

memory = []
pos = 0

for i in range(50000000):
    pos = (pos + step_size)%(i)+1 if i != 0 else 0
    if(pos == 1):
        print(i)
    if(i%500000 == 0):
        print(i/500000)

print(memory[1])
