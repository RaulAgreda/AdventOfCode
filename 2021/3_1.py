import ReadInput

lines = ReadInput.convert("3_Input.txt")

def decode(bitStr):
    decimal = 0

    for i in range(len(bitStr)):
        decimal += 2**(len(bitStr) - 1 - i) * int(bitStr[i])

    return decimal

def notDoor(bitStr):
    result = ""

    for b in bitStr:
        result+= "0" if b == "1" else "1"
    
    return result

gamma = ""

for i in range(len(lines[0])):
    n0s = 0
    for bitStr in lines:
        if bitStr[i] == "0":
            n0s+=1
    
    gamma += "0" if n0s > len(lines) / 2 else "1"

epsilon = notDoor(gamma)

print(decode(gamma) * decode(epsilon))

