import ReadInput

lines = ReadInput.convert("12_Input.txt")

cavePaths = {"start":set(),"end":set()}

for line in lines:
    conn = line.split("-")

    if conn[0] not in cavePaths.keys():
        cavePaths[conn[0]] = set()
    if conn[1] not in cavePaths.keys():
        cavePaths[conn[1]] = set()        

    if conn[1] not in cavePaths[conn[0]]:
        cavePaths[conn[0]].add(conn[1])
    if conn[0] not in cavePaths[conn[1]]:
        cavePaths[conn[1]].add(conn[0])

def part1():

    def getPaths(cavePahts):
        visited = set()
        visited.add("start")
        total = 0
        for k in cavePaths["start"]:
            total+=_getPaths(cavePaths,k,visited)

        return total
                
    def _getPaths(cavePaths,current,visited):
        visited = visited.copy()
        if current == "end":
            return 1
        else:
            if current == str.lower(current):
                visited.add(current)

            total = 0
            for k in cavePaths[current]:
                if k not in visited:
                    total += _getPaths(cavePaths,k,visited)

            return total

    return getPaths(cavePaths)

def part2():

    allPaths = set()
    # Introducir programación dinámica para más eficiencia

    def getPaths(cavePaths):
        visited = {}
        visited["start"] = True
        total = 0
        for k in cavePaths["start"]:
            total +=_getPaths(cavePaths,k,visited)

        return total
                
    def _getPaths(cavePaths,current, visited):
        visited = visited.copy()
        if current == "end":
            return 1
        else:
            if current == str.lower(current):
                if current not in visited:
                    visited[current] = False
                else:
                    visited[current] = True

            total = 0
            for k in cavePaths[current]:
                if k not in visited or visited[k] == False:
                    total += _getPaths(cavePaths,k,visited)

            return total

    return getPaths(cavePaths)

print(part1())
