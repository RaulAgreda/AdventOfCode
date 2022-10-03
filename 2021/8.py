import ReadInput

def part1():
    lines = ReadInput.convert("8_Input.txt")
    outputs = []
    for line in lines:
        output = line.split(" | ")[1].split(" ")
        outputs.append(output)

    # print(outputs)
    total = 0
    for output in outputs:
        for out in output:
            lngth = len(out)
            if lngth in (2,3,4,7):
                # print(out)
                total+=1

    return total

def part2():
    lines = ReadInput.convert("8_Input.txt")
    inputs = []
    outputs = []
    for line in lines:
        separate = line.split(" | ")
        inputs.append(separate[0].split(" "))
        outputs.append(separate[1].split(" "))

    total = 0

    for ind in range(len(lines)):

        def minus(str1,str2):
            for c in str2:
                str1 = str1.replace(c,"")
            return str1

        def getNumber(numbersDic,chain):
            for n in numbersDic.keys():
                if len(numbersDic[n]) == len(chain):
                    isNumber = True
                    for c in chain:    
                        if c not in numbersDic[n]:
                            isNumber = False
                    if isNumber:
                        return n

        numbersBylen = {2:[],3:[],4:[],5:[],6:[],7:[]}
        numbers = {}

        # 1, 4, 7 and 8
        for inp in inputs[ind]:
            if len(inp) == 2:
                numbers[1] = inp
            elif len(inp) == 3:
                numbers[7] = inp
            elif len(inp) == 4:
                numbers[4] = inp
            elif len(inp) == 7:
                numbers[8] = inp
            numbersBylen[len(inp)].append(inp)
        
        # 2, 3 and 5
        for chain in numbersBylen[5]:
            subs = minus(numbers[4],chain)
            # 2 and segment 1
            if len(subs) == 2:
                numbers[2] = chain
            # 3 or 5
            else:
                sub2 = minus(subs,numbers[1])
                # 5
                if sub2 == "":
                    numbers[5] = chain
                # 3
                else:
                    numbers[3] = chain

        # 0, 6 and 9
        for chain in numbersBylen[6]:
            sub = minus(numbers[8],chain)
            # 6
            if minus(sub,numbers[1]) == "":
                numbers[6] = chain
            else:
                # 0 and segment 3
                if minus(sub,numbers[4]) == "":
                    numbers[0] = chain
                # 9
                else:
                    numbers[9] = chain
        
        output = 0

        for i in range(len(outputs[ind])):
            output += getNumber(numbers,outputs[ind][i]) * 10**(len(outputs[0]) - i - 1)

        total+= output
    return total


print(part2())