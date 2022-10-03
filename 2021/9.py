import ReadInput

def part1():
    lines = ReadInput.convert("9_Input.txt")

    rows = {}
    for i in range(len(lines)):
        rows[i] = lines[i]

    def inRange(M,i,j):
        return 0 <= i < len(M) and 0 <= j < len(M[i])

    def checkAdjacent(M,i,j):
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        val = int(M[i][j])
        for dir in directions:
            if inRange(M,i+dir[0],j+dir[1]):
                if int(M[i+dir[0]][j+dir[1]]) <= val:
                    return False
        return True

    mins = {}
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if checkAdjacent(rows,i,j):
                mins[(i,j)] = rows[i][j]
    
    total = 0

    # print(mins)
    for key in mins.keys():
        total += int(mins[key]) + 1
    
    return total

def part2():
    # parte 1 :v
    lines = ReadInput.convert("9_Input.txt")

    rows = {}
    for i in range(len(lines)):
        rows[i] = lines[i]

    def inRange(M,i,j):
        return 0 <= i < len(M) and 0 <= j < len(M[i])

    def checkAdjacent(M,i,j):
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        val = int(M[i][j])
        for dir in directions:
            if inRange(M,i+dir[0],j+dir[1]):
                if int(M[i+dir[0]][j+dir[1]]) <= val:
                    return False
        return True

    mins = set()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if checkAdjacent(rows,i,j):
                mins.add((i,j))

    # Aquí empieza la 2 realmente :v

    def getBasin(M,i,j):
        visited = set()
        visited.add((i,j))

        directions = ((1,0),(-1,0),(0,1),(0,-1))
        for dire in directions:
            propagueBasin(M,i+dire[0],j+dire[1],visited)

        return len(visited)

    def propagueBasin(M,i,j,visited):
        
        if not (i,j) in visited and inRange(M,i,j) and not M[i][j] == "9":

            directions = ((1,0),(-1,0),(0,1),(0,-1))
            visited.add((i,j))
            
            for dire in directions:
                propagueBasin(M,i+dire[0],j+dire[1],visited)

        return

    total = 1

    allBasins = []

    for coord in mins:
        allBasins.append(getBasin(rows,coord[0],coord[1]))
    for i in range(3):
        mayorBasin = max(allBasins)
        allBasins.remove(mayorBasin)
        total*=mayorBasin
        
    return total

print(part2())