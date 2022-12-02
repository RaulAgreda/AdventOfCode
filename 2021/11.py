import ReadInput

def inRange(M,i,j):
        return 0 <= i < len(M) and 0 <= j < len(M[i])


# Diccionario  con todas las posiciones y el valor actual
octopuses = {}
# Diccionario con un set de todos los adyacentes a una posición. (Porque soy vago)
adjacents = {}

lines = ReadInput.convert("11_Input.txt")

# Set octopuses
for i in range(len(lines)):
    for j in range(len(lines[i])):
        octopuses[(i,j)] = int(lines[i][j])

# Set adjacents
for i in range(len(lines)):
    for j in range(len(lines[i])):
        directions = ((-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,1),(1,0),(1,-1))

        adjacents[(i,j)] = set()

        for dire in directions:
            if inRange(lines,i+dire[0],j+dire[1]):
                adjacents[(i,j)].add((i+dire[0],j+dire[1]))

def part1():
    total = 0

    for it in range(100):
        flashes = set()

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                octopuses[(i,j)] += 1
                if octopuses[(i,j)] == 10:
                    octopuses[(i,j)] = 0
                    flashes.add((i,j))
                    total+=1

        while len(flashes) > 0:
            flash = flashes.pop()
            for adjacent in adjacents[flash]:
                if octopuses[adjacent] != 0:
                    octopuses[adjacent] += 1

                    if octopuses[adjacent] == 10:
                        octopuses[adjacent] = 0
                        flashes.add(adjacent)
                        total+=1

    return total

def part2():
    iteration = 1

    # jejejjejejjeje
    while True:

        flashes = set()
        total = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                octopuses[(i,j)] += 1
                if octopuses[(i,j)] == 10:
                    octopuses[(i,j)] = 0
                    flashes.add((i,j))
                    total+=1

        while len(flashes) > 0:
            flash = flashes.pop()
            for adjacent in adjacents[flash]:
                if octopuses[adjacent] != 0:
                    octopuses[adjacent] += 1

                    if octopuses[adjacent] == 10:
                        octopuses[adjacent] = 0
                        flashes.add(adjacent)
                        total+=1

        if total == 100:
            return iteration
        else:
            iteration+=1

print(part1())