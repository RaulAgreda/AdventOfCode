import ReadInput
code = ReadInput.convert("8_Input","\n")

def getInstruction(code,line):
    instructions = code[line].split()
    return instructions[0],int(instructions[1])

# Part 1
# nExecutions = [0] * len(code)
# acc = 0
# i = 0
# while i < len(code):
#     nExecutions[i]+=1
#     if nExecutions[i] == 2:
#         break
#     else:
#         instruction = getInstruction(i)
#         if instruction[0] == "acc":
#             acc += instruction[1]
#         elif instruction[0] == "jmp":
#             i += instruction[1]
#             continue
            
#     i+=1

# print(acc)

def checkNewCode(newCode):
    nExecutions = [0] * len(code)

    acc = 0
    i = 0
    while i < len(newCode):
        nExecutions[i]+=1
        if nExecutions[i] == 2:
            # print(i)
            return

        instruction = getInstruction(newCode,i)
        if instruction[0] == "acc":
            acc += instruction[1]
        elif instruction[0] == "jmp":
            i += instruction[1]
            continue
            
        i+=1
    
    print(acc)

for i in range(len(code)):
    inst = getInstruction(code,i)
    if inst[0] == "nop" or inst[0] == "jmp":
        newCode = code.copy()
        newCode[i] = ("jmp" if inst[0] == "nop" else "nop") + (" +" if inst[1] > 0 else " ") + str(inst[1])
        # print("Checking new code",newCode)
        checkNewCode(newCode)


