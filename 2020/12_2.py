import ReadInput
import math

def getDirection(text):
    dir = text[0]
    units = int(text[1:])
    return dir, units


inp = ReadInput.convert("12_Input.txt")

shipPosition = [0,0]
waypoint = [1,10]

def moveWaypoint(direction,distance):
    if direction in "NS":
        waypoint[0] += distance * (1 if direction == "N" else -1)
    elif direction in "EW":
        waypoint[1] += distance * (1 if direction == "E" else -1)

for s in inp:
    print(s)

    coord,dist = getDirection(s)

    if coord in "RL":
        if dist == 180:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
        elif dist == 90:
            copy = tuple(waypoint)

            waypoint[0] = -copy[1] if coord == "R" else copy[1]
            waypoint[1] = copy[0] if coord == "R" else -copy[0]
        elif dist == 270:
            copy = tuple(waypoint)

            waypoint[0] = -copy[1] if coord == "L" else copy[1]
            waypoint[1] = copy[0] if coord == "L" else -copy[0]
        
    elif coord in "NSEW":
        moveWaypoint(coord,dist)
    elif coord == "F":
        
        shipPosition[0] += dist * waypoint[0]
        shipPosition[1] += dist * waypoint[1]
        



    print("ShipPos: ",shipPosition)
    print("Waypoint: ",waypoint)

    
    
print(abs(shipPosition[0]) + abs(shipPosition[1]))



