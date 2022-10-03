import ReadInput

def getDirection(text):
    dir = text[0]
    units = int(text[1:])
    return dir, units


inp = ReadInput.convert("12_Input.txt")

position = [0,0]
facing = 1

card = ("N","E","S","W")

def move(direction,distance):
    if direction in "NS":
        position[0] += distance * (1 if direction == "N" else -1)
    elif direction in "EW":
        position[1] += distance * (1 if direction == "E" else -1)

    

for s in inp:
    print("currentFacing: ",card[facing])
    print(s)

    coord,dist = getDirection(s)

    if coord in "RL":
        facing = (facing + (1 if coord == "R" else -1) * dist//90) % 4
        #print(coord,dist,card[facing])
    elif coord in "NSEW":
        move(coord,dist)
    elif coord == "F":
        move(card[facing],dist)

    print(position)

    
    
print(abs(position[0]) + abs(position[1]))



