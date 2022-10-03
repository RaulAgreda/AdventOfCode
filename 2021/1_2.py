import ReadInput

lista = ReadInput.convertToInt("1_Input.txt")


prev = lista[0] + lista[1] + lista[2]

total = 0

for i in range(1,len(lista)-2):
    summ = lista[i] + lista[i+1] + lista[i+2]
    if summ > prev:
        total+=1
    prev = summ
print(total)