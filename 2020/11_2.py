import ReadInput

matrix = ReadInput.convert("11_Input.txt")
for i in range(len(matrix)):
    line = matrix[i]
    matrix[i] = []
    for c in line:
        matrix[i].append(c)

def inMatrix(i,j,m):
    return i >= 0 and i < len(m) and j >= 0 and j < len(m[i])

def updateMatrix(updates):
    for u in updates:
        matrix[u[0]][u[1]] = u[2]

def countOccupied(m,i,j):
    dirs = ((1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1))
    
    total = 0
    for d in dirs:
        k = 1
        while inMatrix(i+k*d[0],j+k*d[1],matrix):
            elem = m[i+k*d[0]][j+k*d[1]]
            if elem in "#L":
                if elem == "#":
                    total+=1
                break
            k+=1

    return total
for line in matrix:
    print(line)
    print("")
# print(countOccupied(matrix,0,2))
different = True
while(different):
    different = False

    newChanges = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != ".":
                adjacent = countOccupied(matrix,i,j)
                # print(adjacent)

                if matrix[i][j] == "L" and adjacent == 0:
                    newChanges.append([i,j,"#"])
                    different = True
                elif matrix[i][j] == "#" and adjacent >= 5:
                    newChanges.append([i,j,"L"])
                    different = True

    if different:
        updateMatrix(newChanges)
        for line in matrix:
            print(line)
        print("")

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(matrix[i][j] == "#"):
            total+=1

print(total)