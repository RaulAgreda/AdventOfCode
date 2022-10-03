import ReadInput

lista = ReadInput.convertToInt("1_Input.txt")


prev = lista[0]

total = 0

for i in range(1,len(lista)):
    summ = lista[i]
    if summ > prev:
        total+=1
    prev = summ
    
print(total)

