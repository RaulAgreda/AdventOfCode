import ReadInput

def printMarcs(marcs):

    maxX = 0
    maxY = 0

    for coord in marcs:
        if coord[0] > maxX:
            maxX = coord[0]
        if coord[1] > maxY:
            maxY = coord[1]
    
    for j in range(maxY + 1):
        for i in range(maxX + 1):
            print(("#" if (i,j) in marcs else "."),end = "")
        print("")
    print("")



def part1():

    lines = ReadInput.convert("13_Input.txt")

    marcs = set()

    folds = [None]

    for line in lines:
        if line == "":
            folds.pop()
            continue
        if len(folds) == 1 and folds[0] == None:
            part = line.split(",")
            marcs.add((int(part[0]),int(part[1])))
        else:
            folds.append(line)

    # for fold in folds:
    fold = folds[0]
    n = int(fold[13:])
    if "x" in fold:
        for marc in marcs.copy():
            if marc[0] > n:
                marcs.add((n - marc[0] + n,marc[1]))
                marcs.remove(marc)
    else:
        for marc in marcs.copy():
            if marc[1] > n:
                marcs.add((marc[0],n - marc[1] + n))
                marcs.remove(marc)
    

    

    return len(marcs)


    

def part2():

    lines = ReadInput.convert("13_Input.txt")

    marcs = set()

    folds = [None]

    for line in lines:
        if line == "":
            folds.pop()
            continue
        if len(folds) == 1 and folds[0] == None:
            part = line.split(",")
            marcs.add((int(part[0]),int(part[1])))
        else:
            folds.append(line)

    for fold in folds:
    
        n = int(fold[13:])
        if "x" in fold:
            for marc in marcs.copy():
                if marc[0] > n:
                    marcs.add((n - marc[0] + n,marc[1]))
                    marcs.remove(marc)
        else:
            for marc in marcs.copy():
                if marc[1] > n:
                    marcs.add((marc[0],n - marc[1] + n))
                    marcs.remove(marc)

        printMarcs(marcs)

    return len(marcs)

print(part2())