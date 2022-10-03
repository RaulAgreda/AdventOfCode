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
        if mask[i] == "X":
            result+=bitStr[i]
        else:
            result+=mask[i]
    return decode(result)

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

mem = {}

maskMems = {}

for line in lines:
    if "mask" in line:

        for key in maskMems.keys():
            mem[key] = applyMask(maskMems[key],mask)

        maskMems = {}
        mask = line.split(" ")[2]
    else:
        instruction = line.split(" ")
        memoryPos = instruction[0]
        memoryPos = memoryPos[4:-1]
        # print(memoryPos)
        memoryPos = int(memoryPos)

        mem[memoryPos] = int(instruction[2])

        maskMems[memoryPos] = mem[memoryPos]

for key in maskMems.keys():
    mem[key] = applyMask(maskMems[key],mask)

total = 0

for key in mem.keys():
    total += mem[key]

print(total)