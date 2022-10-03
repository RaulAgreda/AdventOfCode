import ReadInput
import math

sketch = ReadInput.convert("13_Input.txt")

busIDs = sketch[1].split(",")

for i in range(len(busIDs)):
    if busIDs[i] != "x":
        busIDs[i] = int(busIDs[i])


firstBus = busIDs[0]

buses = {}

for i in range(len(busIDs)):
    if busIDs[i] != 'x':
        buses[i] = busIDs[i]

print(buses)

t = firstBus
w = firstBus

it = 0

for key in buses.keys():
    if buses[key] != firstBus:
        i = 1
        found = False
        while not found:
            if (t + w * i + key) % buses[key] == 0:
                found = True
                
                t += w*i
                w *= buses[key]
            else:
                i+=1

            it+=1

print(t,it)
