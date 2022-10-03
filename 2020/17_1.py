import ReadInput

layer = ReadInput.convert("17_Input.txt")

# Generar desfases de los vecinos
neigCoords = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            neigCoords.append((i-1,j-1,k-1))
#print(neigCoords)
#neigCoords.remove((0,0,0))
# La idea es añadir al diccionario solo los #, para así comprobar los vecinos de estos y ya.
print(len(neigCoords))
print(neigCoords)
cubes = {}

for i in range(len(layer)):
    for j in range(len(layer[i])):
        if layer[len(layer) - 1- i][j] == "#":
            cubes[(j,i,0)] = "#"




print(cubes)

for i in range(6):
    changes = {}
    for key in cubes.keys():
        for direct in neigCoords:
                # change current and neighbours values
                neig = (key[0]+direct[0],key[1]+direct[1],key[2]+direct[2])
                
                if neig not in changes.keys():
                    #print("checking coord",neig)
                    neigCount = 0
                    # check neighbours #
                    for dir2 in neigCoords:
                        neig2 = (neig[0]+dir2[0],neig[1]+dir2[1],neig[2]+dir2[2])
                        if dir2 != (0,0,0) and neigCount <= 3:
                            if neig2 in cubes.keys():
                                #print(neig2)
                                neigCount+=1

                    if neig in cubes.keys():
                        if neigCount == 2 or neigCount == 3:
                            changes[neig] = "#"
                        else:
                            changes[neig] = "."
                    else:
                        if neigCount == 3:
                            changes[neig] = "#"
                        else:
                            changes[neig] = "."

    for key in changes.keys():
        if changes[key] == "#":
            cubes[key] = "#"
        elif key in cubes.keys():
            cubes.pop(key)

print(len(cubes.keys()))


                            


                            

