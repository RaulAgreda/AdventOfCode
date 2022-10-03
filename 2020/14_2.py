import ReadInput

lines = ReadInput.convert("14_Input.txt")

def code(decimal):
    bitStr = ""

    while decimal > 0:
        
        bitStr += str(decimal%2)
        decimal = decimal //2
    for i in range(len(bitStr),36):
        bitStr+="0"

    return bitStr[::-1]

def decode(bitStr):
    decimal = 0

    for i in range(len(bitStr)):
        decimal += 2**(len(bitStr) - 1 - i) * int(bitStr[i])

    return decimal
    
def applyMask(decimal,mask):
    bitStr = code(decimal)
    result = ""
    for i in range(36):
        if mask[i] == "0":
            result+=bitStr[i]
        else:
            result+=mask[i]
    return result

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

mem = {}

maskMems = {}

def applyMaskToMem():
    for key in maskMems.keys():
            newList = []
            mem[key] = applyMask(maskMems[key],mask)
            getAllFloatingNumbers(mem[key], newList)
            mem[key] = newList


def getNextFloatingNumbers(bitStr):
    return bitStr.replace("X","0",1), bitStr.replace("X","1",1)

def getAllFloatingNumbers(bitStr,lista):

    if bitStr.count("X") != 0:
        next = getNextFloatingNumbers(bitStr)
        final = getAllFloatingNumbers(next[0],lista), getAllFloatingNumbers(next[1],lista)
        if final[0] != None:
            #print(final)
            lista.append(final[0])
            lista.append(final[1])    
    else:
        #print(bitStr)
        return bitStr

for line in lines:
    if "mask" in line:
        maskMems = {}
        mask = line.split(" ")[2]
    else:
        instruction = line.split(" ")
        memoryPos = instruction[0]
        # Extract memoryPosition
        memoryPos = memoryPos[4:-1]
        memoryPos = int(memoryPos)
        # Apply value to memory position
        value = int(instruction[2])
        newList = []
        maskedValue = applyMask(memoryPos,mask)
        getAllFloatingNumbers(maskedValue, newList)
        
        for adress in newList:
            mem[adress] = value

total = 0

for key in mem.keys():
    total += mem[key]

print(total)