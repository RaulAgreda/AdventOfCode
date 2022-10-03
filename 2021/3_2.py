import ReadInput

lines = ReadInput.convert("3_Input.txt")

def decode(bitStr):
    decimal = 0

    for i in range(len(bitStr)):
        decimal += 2**(len(bitStr) - 1 - i) * int(bitStr[i])

    return decimal


def mostCommon(bitList,i):
    n0s = 0

    for bitStr in bitList:
        if bitStr[i] == "0":
            n0s+=1
    
    return "0" if n0s > len(bitList) / 2 else "1"

def search(bitList,most = True):
    result = bitList.copy()

    for i in range(len(result[0])):
        valid = []
        common = mostCommon(result,i)
        if not most:
            common = "0" if common == "1" else "1"
        for b in range(len(result)):
            if common == result[b][i]:
                valid.append(result[b])
        
        if len(valid) == 1:
            return valid[0]
        else:
            result = valid.copy()



o2R = search(lines)
print(o2R)
co2 = search(lines,False)
print(co2)
print(decode(o2R) * decode(co2))