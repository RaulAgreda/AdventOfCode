import ReadInput
import math

sketch = ReadInput.convert("13_Input.txt")

myDepart = int(sketch[0])
busIDs = []

ids = sketch[1].split(",")

for c in ids:
    if c != "x":
        busIDs.append(int(c))

busDeparts = []

for bus in busIDs:
    coef = math.ceil(myDepart/bus)
    busDeparts.append(bus*coef)

minDepart = min(busDeparts)
selectedBus = busIDs[busDeparts.index(minDepart)]

print((minDepart - myDepart) * selectedBus)
