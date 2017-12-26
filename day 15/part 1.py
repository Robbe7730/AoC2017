genA = 516
genB = 190
count = 0

for i in range(40000000):
    genA = (genA*16807)%2147483647
    genB = (genB*48271)%2147483647
    if(genA % 65536 == genB % 65536):
        count += 1
        print(i)
print(count)
