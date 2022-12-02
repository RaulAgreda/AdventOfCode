import ReadInput

def part1():

    fuels = ReadInput.convert("7_Input.txt")[0]
    crabs = [int(c) for c in fuels.split(",")]
    # print(fuels)
    possible = set()
    for pos in range(min(crabs),max(crabs)+1):
        total = 0
        for crabPos in crabs:
            total += abs(crabPos-pos)
        possible.add(total)

    return min(possible)

def part2():
    fuels = ReadInput.convert("7_Input.txt")[0]
    crabs = [int(c) for c in fuels.split(",")]
    # print(fuels)
    sumMem = {}
    def sumF(n,sumM):
        if n in sumMem.keys():
            return sumMem[n]
        else:
            total = 0
            for i in range(1,n+1):
                total+=i
            sumMem[n] = total
            return total

    possible = set()
    for pos in range(min(crabs),max(crabs)+1):
        total = 0
        for crabPos in crabs:
            total += sumF(abs(crabPos-pos),sumMem)
        possible.add(total)

print(part1())