import ReadInput
codes = ReadInput.convert("5_Input")

ids = []

def roundN(self):
    return int(self) if self - int(self) < 0.5 else int(self) + 1

for code in codes:
    # print("\n",code)
    pos = [0,127]
    for i in range(len(code)):
        if code[i] in "FL":
            pos[1] = pos[1] - roundN((pos[1] - pos[0]) / 2)
        elif code[i] in "BR":
            pos[0] = pos[0] + roundN((pos[1] - pos[0]) / 2)
        if i == 6:
            row = pos[0]
            pos = [0,7]

    column = pos[0]
    # if 0 < row < 127:
    ids.append(row * 8 + column)

# print(ids)
# print(max(ids))
myList = []

for seat in ids:
    if seat + 1 in ids or seat - 1 in ids:
        myList.append(seat)
print(myList)
for i in range(min(myList),max(myList)):
    if i not in myList:
        print(i)