from typing import *
from template.problem import Problem

class Day12(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def part1(self):
        visited = set()
        # areaId: (perimeter, area)
        measures = {}
        areaId = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if (i,j) in visited:
                    continue
                pa = self.measurePandA(self.input[i][j], i, j, visited)
                measures[areaId] = pa
                areaId += 1
        total = 0
        for aId in measures:
            total += measures[aId][0] * measures[aId][1]
        return total
    
    def measurePandA(self, areaChar, i, j, visited:set):
        if i < 0 or j < 0 or i >= len(self.input) or j >= len(self.input[0]):
            return 1, 0
        if areaChar != self.input[i][j]:
            return 1, 0
        if (i,j) in visited:
            return 0, 0
        visited.add((i,j))
        u = self.measurePandA(areaChar, i-1, j, visited)
        d = self.measurePandA(areaChar, i+1, j, visited)
        l = self.measurePandA(areaChar, i, j-1, visited)
        r = self.measurePandA(areaChar, i, j+1, visited)
        return u[0] + d[0] + l[0] + r[0], u[1] + d[1] + l[1] + r[1] + 1

    def getArea(self, areaChar, i, j, visited: set):
        if not self.inBounds(i, j):
            return
        if areaChar != self.input[i][j]:
            return
        if (i,j) in visited:
            return
        visited.add((i,j))
        self.getArea(areaChar, i-1, j, visited)
        self.getArea(areaChar, i+1, j, visited)
        self.getArea(areaChar, i, j-1, visited)
        self.getArea(areaChar, i, j+1, visited)
        return visited
        
    def inBounds(self, i,j):
        return i >= 0 and j >= 0 and i < len(self.input) and j < len(self.input[0])
    
    def countCorners(self, area:set):
        ulCheck = [(-1, 0), (0, -1), (-1, -1)]
        urCheck = [(-1, 0), (0, 1), (-1, 1)]
        dlCheck = [(1, 0), (0, -1), (1, -1)]
        dRCheck = [(1, 0), (0, 1), (1, 1)]
        # for ul, 
        # if left and up not in area is outer corner
        # elif left and up in area but diagonal not, inner corner
        n_corners = 0
        for i,j in area:
            for corner in (ulCheck, urCheck, dlCheck, dRCheck):
                s1 = self.sumTuples((i, j), corner[0])
                s2 = self.sumTuples((i, j), corner[1])
                d = self.sumTuples((i, j), corner[2])
                if s1 not in area and s2 not in area:
                    n_corners+=1
                elif s1 in area and s2 in area and d not in area:
                    n_corners+=1
        return n_corners

    def sumTuples(self,t1,t2):
        return tuple([t1[i] + t2[i] for i in range(len(t1))])

    def part2(self):
        total = 0
        alreadyVisited = set()
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if (i,j) not in alreadyVisited:
                    a = self.getArea(self.input[i][j], i, j , set())
                    alreadyVisited |= a
                    total += len(a) * self.countCorners(a)
        return total
