import ReadInput

count = 0

# Part 1
# for password in ReadInput.convert("2_Input"):
    
#     elements = password.split()
#     minim,maxim = elements[0].split("-")

#     minim = int(minim)
#     maxim = int(maxim)
    
#     letter = elements[1][0]

#     actualPassword = elements[2]

#     if minim <= actualPassword.count(letter) <= maxim:
#         count+=1

# Part 2
for password in ReadInput.convert("2_Input"):
    
    elements = password.split()
    pos1,pos2 = elements[0].split("-")

    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    
    letter = elements[1][0]

    actualPassword = elements[2]


    if (actualPassword[pos1] == letter or actualPassword[pos2] == letter) and actualPassword[pos1] != actualPassword[pos2]:
        count+=1

print(count)
