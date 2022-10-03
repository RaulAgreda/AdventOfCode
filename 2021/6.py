import ReadInput

def part1():
    inp = ReadInput.convert("6_Input.txt")[0]

    fishes = []

    for c in inp:
        if c != ",":
            fishes.append(int(c))
    # print(fishes)

    for day in range(80):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1

    # print(fishes)
    return len(fishes)

def part2():
    inp = ReadInput.convert("6_Input.txt")[0]

    fishes = {}
    
    for i in range(9):
        fishes[i] = 0

    for c in inp:
        if c != ",":
            fishes[int(c)] += 1

    for day in range(256):
        newFishes = 0
        for key in fishes.keys():
            if key == 0:
                newFishes = fishes[0]
            if key != 8:
                fishes[key] = fishes[key+1]
            else:
                fishes[6] += newFishes
                fishes[8] = newFishes
    
    total = 0
    for key in fishes.keys():
        total += fishes[key]

    return total

    

print(part2())