import ReadInput
code = ReadInput.convertToInt("9_Input")
# print(code)
# Step 1
number = 0
preamble = []

for i in range(25):
    preamble.append(code[i])

for i in range(25,len(code)):
    hasProperty = False
    for j in range(len(preamble) - 25,len(preamble)):
        for k in range(len(preamble) - 25,len(preamble)):
            if j != k and code[i] == preamble[j] + preamble[k]:
                hasProperty = True
                break
        if hasProperty:
            break
    preamble.append(code[i])
    if not hasProperty:
        number = code[i]
        print(code[i],"no cumple zorra")


add = 0
i = 0
save = 0
addList = []
while i < len(code):
    if add == 0:
        addList = []
        i = save
        save = i + 1  
    add += code[i]
    addList.append(code[i])
    i+=1
    if add > number:
        add = 0
    elif add == number:
        print("Found it :D")
        break

print(addList,min(addList) + max(addList))