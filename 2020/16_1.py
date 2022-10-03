inp = open("16_Input.txt").read()

inp = inp.split("\n")

validNumbers = {}

rangesList = []

yourTicketIndx = 0
# Extract ranges
for i in range(len(inp)):
    if "or" in inp[i]:

        line = inp[i]
        
        ranges = inp[i][line.index(": ") + 2:]
        ranges = tuple(ranges.split(" or "))
        # print(ranges)

        for cRange in ranges:
            # print(cRange)
            rang = cRange.split("-")
            rangesList.append((int(rang[0]),int(rang[1])))
    else:
        break

def inRange(rang,n):
    return rang[0] <= n and n <= rang[1]

invalidValues = []

# Extract nearby tickets
ind = inp.index("nearby tickets:") + 1
for i in range(ind,len(inp)):
    line = inp[i].split(",")
    for n in line:
        isValid = False
        for rang in rangesList:
            # print(n)
            if inRange(rang,int(n)):
                isValid = True
        if not isValid:
            invalidValues.append(int(n))
# print(invalidValues)
print(sum(invalidValues))