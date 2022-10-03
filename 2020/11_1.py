import ReadInput

matrix = ReadInput.convert("11_Input.txt")
for i in range(len(matrix)):
    line = matrix[i]
    matrix[i] = []
    for c in line:
        matrix[i].append(c)

def getAdjacentCount(i,j,matrix):
    """return empty, occupied"""
    empty = 0
    occupied = 0

    for k in range(-1,2):
        for k2 in range(-1,2):
            if not(k == 0 and k2 == 0):
                if (i + k >= 0 and i + k < len(matrix) and j + k2 >= 0 and j + k2 < len(matrix[0])):                   
                    if matrix[i+k][j+k2] == "#":
                        occupied+=1
                    elif matrix[i+k][j+k2] == "L":
                        empty+=1
          
    return empty, occupied

prevMatrix = []
nIt = 0
different = True
while(different):
    # prevMatrix = matrix
    prevMatrix = []
    for line in matrix:
        prevMatrix.append(line.copy())

    different = False

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != ".":
                adjacent = getAdjacentCount(i,j,prevMatrix)
                if matrix[i][j] == "L" and adjacent[1] == 0:
                    matrix[i][j] = "#"
                    different = True
                elif matrix[i][j] == "#" and adjacent[1] >= 4:
                    matrix[i][j] = "L"
                    different = True
    
total = 0

for line in matrix:
    total+=line.count("#")
print(total,nIt)
        