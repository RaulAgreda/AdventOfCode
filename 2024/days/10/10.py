from typing import *
from template.problem import Problem

class Day10(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def part1(self):
        tMap = []
        for line in self.input:
            tMap.append([int(x) for x in line])
        total = 0
        for i in range(len(tMap)):
            for j in range(len(tMap[0])):
                if tMap[i][j] == 0:
                    total += self.getPaths1(tMap, i, j, -1, set())
        return total
        
    def getPaths1(self, tMap, i, j, prev, visited: set):
        if i < 0 or j < 0 or i > len(tMap) - 1 or j > len(tMap) - 1:
            return 0
        if tMap[i][j] != prev + 1:
            return 0
        if tMap[i][j] == 9:
            if (i,j) not in visited:
                visited.add((i, j))
                return 1
            else:
                return 0
        total = 0
        total += self.getPaths1(tMap, i+1, j, tMap[i][j], visited)
        total += self.getPaths1(tMap, i, j+1, tMap[i][j], visited)
        total += self.getPaths1(tMap, i-1, j, tMap[i][j], visited)
        total += self.getPaths1(tMap, i, j-1, tMap[i][j], visited)
        return total


    def part2(self):
        tMap = []
        for line in self.input:
            tMap.append([int(x) for x in line])
        total = 0
        for i in range(len(tMap)):
            for j in range(len(tMap[0])):
                if tMap[i][j] == 0:
                    total += self.getPaths2(tMap, i, j, -1)
        return total
    
    def getPaths2(self, tMap, i, j, prev):
        if i < 0 or j < 0 or i > len(tMap) - 1 or j > len(tMap) - 1:
            return 0
        if tMap[i][j] != prev + 1:
            return 0
        if tMap[i][j] == 9:
            return 1
        total = 0
        total += self.getPaths2(tMap, i+1, j, tMap[i][j])
        total += self.getPaths2(tMap, i, j+1, tMap[i][j])
        total += self.getPaths2(tMap, i-1, j, tMap[i][j])
        total += self.getPaths2(tMap, i, j-1, tMap[i][j])
        return total
