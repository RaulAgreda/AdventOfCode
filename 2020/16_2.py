"""Este ejercicio va de que cada columna pertenece a una categoría entonces hay que ver el orden en el que aparecen las categorías en función de las columnas
Y luego ver a qué categorías pertenecen las columnas de mi ticket"""

inp = open("16_Input.txt").read()

inp = inp.split("\n")

validNumbers = {}

rangesList = []

yourTicketIndx = 0

fields = []

# Extract ranges
for i in range(len(inp)):
    if "or" in inp[i]:
        fields.append(None)
        line = inp[i]
        
        ranges = inp[i][line.index(": ") + 2:]
        ranges = tuple(ranges.split(" or "))

        for cRange in ranges:
            rang = cRange.split("-")
            rangesList.append((int(rang[0]),int(rang[1])))
    else:
        yourTicketIndx = i + 2
        break

def inRange(rang,n):
    return rang[0] <= n and n <= rang[1]

validValues = []

# Extract nearby tickets
ind = inp.index("nearby tickets:") + 1
for i in range(ind,len(inp)):
    line = inp[i].split(",")
    validValues.append([])
    for n in line:
        validValues[i-ind].append(int(n))
        isValid = False
        for rang in rangesList:
            if inRange(rang,int(n)):
                isValid = True
                
        if not isValid:
            validValues[i-ind][-1] = None


validValuesT = []

# Transpose
for j in range(len(validValues[0])):
    validValuesT.append([])
    for i in range(len(validValues)): 
        validValuesT[j].append(validValues[i][j])


for row in range(len(validValuesT)): # Por cada columna
    posibleFields = []
    for f in range(len(fields)): # Buscamos a qué field pertenece (por índice)           
        isInField = True
        for n in validValuesT[row]:
            #print(n,f)
            if not(n is None or inRange(rangesList[2*f],n) or inRange(rangesList[2*f + 1],n)):
                isInField = False
                #print(n,f)
                break

        if isInField:
            posibleFields.append(f)
                  
    fields[row] = posibleFields.copy()

# Seleccionar a qué field pertenece de sus posibilidades
singleValue = True
sv = None
while singleValue:

    singleValue = False

    for f in range(len(fields)):
        if type(fields[f]) is list and len(fields[f]) == 1:
            singleValue = True
            sv = fields[f][0]
            fields[f] = sv
    
    if singleValue:
        for f in range(len(fields)):
            if type(fields[f]) is list:
                if sv in fields[f]:
                    fields[f].remove(sv)

# Calcular resultado final
# Extract myTicket
myValues = inp[yourTicketIndx].split(",")
for v in range(len(myValues)):
    myValues[v] = int(myValues[v])

total = 1
for i in range(len(myValues)):
    if fields[i] < 6:
        total*=myValues[i]

print(total)

