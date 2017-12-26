genA = 516
genB = 190
count = 0

for i in range(5000000): # 5000000
    genA = (genA*16807)%2147483647
    genB = (genB*48271)%2147483647
    while not genA%4 == 0:
        # print("A")
        genA = (genA*16807)%2147483647
    while not genB%8 == 0:
        # print("B")
        genB = (genB*48271)%2147483647
    # print(genA, genB)
    if(genA % 65536 == genB % 65536):
        count += 1
        print(i)
print(count)
