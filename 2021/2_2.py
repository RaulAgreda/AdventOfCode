import ReadInput

line = ReadInput.convert("2_Input.txt")

position = [0,0,0]

for inst in line:
    instruc = inst.split()
    dir = instruc[0]
    x = int(instruc[1])

    if dir == "forward":
        position[0] += x
        position[1] += position[2] * x
    elif dir == "up":
        position[2] -= x
    elif dir == "down":
        position[2] += x

print(position[0] * position[1])

