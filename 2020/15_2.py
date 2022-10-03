#EXACTAMENTE IGUAL QUE EL 1 PERO CON MÁS ITERACIONES XDDD
#Probablemente haya una forma eficiente en la que vaya follao pero me da palo hacerla y esto funciona no se toma demasiao
myInpS = "8,11,0,19,1,2"
myInpS = myInpS.split(",")
myInp = {}

# Set starting numbers
for n in range(len(myInpS)):
    myInp[int(myInpS[n])] = n+1

lastNumber = 0
# Start at the len + 2
for i in range(len(myInpS)+2,30000001):

    if lastNumber in myInp.keys():
        
        currentNumber = i - 1 - myInp[lastNumber]
        myInp[lastNumber] = i - 1
        lastNumber = currentNumber

    else:
        myInp[lastNumber] = i-1
        lastNumber = 0

    i+=1

print(lastNumber)


