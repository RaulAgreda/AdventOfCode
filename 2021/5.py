import ReadInput

def part1():
    lines = ReadInput.convert("5_Input.txt")

    # Get lines
    for i in range(len(lines)):
        lines[i] = lines[i].split(" -> ")
        lines[i] = lines[i][0].split(","),lines[i][1].split(",")

        for j in range(0,2):
            for k in range(0,2):
                lines[i][j][k] = int(lines[i][j][k])

    # Filter horizontal/vertical

    positions = {}

    for line in lines:
        if line[0][0] == line[1][0]:
            for j in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
                key = (line[0][0],j)
                if key in positions.keys():
                    positions[key] += 1
                else:
                    positions[key] = 1
        elif line[0][1] == line[1][1]:
            for j in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
                key = (j,line[0][1])
                if key in positions.keys():
                    positions[key] += 1
                else:
                    positions[key] = 1

    total = 0

    for key in positions.keys():
        if positions[key] >= 2:
            total+=1

    return total

def part2():
    lines = ReadInput.convert("5_Input.txt")

    # Get lines
    for i in range(len(lines)):
        lines[i] = lines[i].split(" -> ")
        lines[i] = lines[i][0].split(","),lines[i][1].split(",")

        for j in range(0,2):
            for k in range(0,2):
                lines[i][j][k] = int(lines[i][j][k])

    # Filter horizontal/vertical

    positions = {}

    for line in lines:
        if line[0][0] == line[1][0]:
            for j in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
                key = (line[0][0],j)
                if key in positions.keys():
                    positions[key] += 1
                else:
                    positions[key] = 1
        elif line[0][1] == line[1][1]:
            for j in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
                key = (j,line[0][1])
                if key in positions.keys():
                    positions[key] += 1
                else:
                    positions[key] = 1
        else:
            dist = abs(line[0][0] - line[1][0])
            dirX = 1 if line[0][0] < line[1][0] else -1
            dirY = 1 if line[0][1] < line[1][1] else -1
            i = 0
            j = 0

            while i <= dist:
                key = (line[0][0]+i*dirX,line[0][1]+j*dirY)
                if key in positions.keys():
                    positions[key] += 1
                else:
                    positions[key] = 1
                i+=1
                j+=1

    total = 0

    for key in positions.keys():
        if positions[key] >= 2:
            total+=1

    return total
            


print(part2())
