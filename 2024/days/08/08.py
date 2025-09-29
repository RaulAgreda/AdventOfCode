from typing import *
from template.problem import Problem

class Day08(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def inBounds(self, i,j):
        return i >= 0 and j >= 0 and i < len(self.input) and j < len(self.input[0])

    def checkAntinodes(self, positions, antinodeSet: set):
        for a in range(len(positions) - 1):
            for b in range(a+1, len(positions)):
                rowDiff = positions[b][0] - positions[a][0]
                colDiff = positions[b][1] - positions[a][1]
                pos1 = (positions[b][0] + rowDiff, positions[b][1] + colDiff)
                pos2 = (positions[a][0] - rowDiff, positions[a][1] - colDiff)
                if self.inBounds(*pos1):
                    antinodeSet.add(pos1)
                if self.inBounds(*pos2):
                    antinodeSet.add(pos2)

    def part1(self):
        positions = {}
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                v = self.input[i][j]
                if v == '.':
                    continue
                if v not in positions:
                    positions[v] = [(i,j)]
                else:
                    positions[v].append((i,j))
        antinodes = set()
        for key in positions:
            self.checkAntinodes(positions[key], antinodes)
        return len(antinodes)

    def checkAntinodes2(self, positions, antinodeSet: set):
        for a in range(len(positions) - 1):
            for b in range(a+1, len(positions)):
                rowDiff = positions[b][0] - positions[a][0]
                colDiff = positions[b][1] - positions[a][1]
                pos1 = (positions[b][0], positions[b][1])
                f = 1
                while self.inBounds(*pos1):
                    antinodeSet.add(pos1)
                    pos1 = (positions[b][0] + rowDiff * f, positions[b][1] + colDiff * f)
                    f+=1
                pos2 = (positions[a][0], positions[a][1])
                f = 1
                while self.inBounds(*pos2):
                    antinodeSet.add(pos2)
                    pos2 = (positions[a][0] - rowDiff * f, positions[a][1] - colDiff * f)
                    f+=1

    def drawAntinodes(self, antinodes: set):
        for i in range(len(self.input)):
            c = ""
            for j in range(len(self.input[0])):
                if (i,j) in antinodes:
                    c+= "#"
                else:
                    c+= self.input[i][j]
            print(c)



    def part2(self):
        positions = {}
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                v = self.input[i][j]
                if v == '.':
                    continue
                if v not in positions:
                    positions[v] = [(i,j)]
                else:
                    positions[v].append((i,j))
        antinodes = set()
        for key in positions:
            self.checkAntinodes2(positions[key], antinodes)
        self.drawAntinodes(antinodes)
        return len(antinodes)
