myInpS = "8,11,0,19,1,2"
myInpS = myInpS.split(",")
myInp = {}

# Set starting numbers
for n in range(len(myInpS)):
    myInp[int(myInpS[n])] = n+1

lastNumber = 0
# Start at the len + 2
for i in range(len(myInpS)+2,2021):

    if lastNumber in myInp.keys():
        
        currentNumber = i - 1 - myInp[lastNumber]
        myInp[lastNumber] = i - 1
        lastNumber = currentNumber

    else:
        myInp[lastNumber] = i-1
        lastNumber = 0

    i+=1

print(lastNumber)


