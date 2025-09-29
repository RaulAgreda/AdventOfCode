from typing import *
from template.problem import Problem

class Day06(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        self.input = [list(line) for line in input.split("\n")]
        self.HEIGHT = len(self.input)
        self.WIDTH = len(self.input[0])
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if self.input[i][j] == "^":
                    self.guard = [i, j]
        
        self.solution = self.part1() if part == '1' else self.part2()
    
    def part1(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        currentDir = 0
        self.input[self.guard[0]][self.guard[1]] = "."
        total = 0
        while not self.leavesTheArea(*self.guard):
            pos = self.input[self.guard[0]][self.guard[1]]
            if pos == ".":
                self.input[self.guard[0]][self.guard[1]] = 'X'
                total += 1
            elif pos == "#":
                self.guard[0] -= directions[currentDir][0]
                self.guard[1] -= directions[currentDir][1]
                currentDir = (currentDir + 1) % 4
            self.guard[0] += directions[currentDir][0]
            self.guard[1] += directions[currentDir][1]
        # Add your solution for part 1 here
        return total
    
    def leavesTheArea(self, i, j):
        return not (0 <= i < self.HEIGHT and 0 <= j < self.WIDTH)

    def part2(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        currentDir = 0
        # self.input[self.guard[0]][self.guard[1]] = "."
        startPos = tuple(self.guard)
        visited = set()
        while not self.leavesTheArea(*self.guard):
            pos = self.input[self.guard[0]][self.guard[1]]
            if pos == "#":
                self.guard[0] -= directions[currentDir][0]
                self.guard[1] -= directions[currentDir][1]
                currentDir = (currentDir + 1) % 4
            else:
                visited.add((self.guard[0], self.guard[1]))

            self.guard[0] += directions[currentDir][0]
            self.guard[1] += directions[currentDir][1]
        visited.remove(startPos)
        total = 0

        for vis in visited:
            if self.simulateMap(startPos, vis):
                if (total % 100 == 0):
                    print(total)
                total += 1

        # Add your solution for part 2 here
        return total
    
    def simulateMap(self, startPosition, obstacle):
        self.guard = list(startPosition)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        currentDir = 0
        visited = set()

        while not self.leavesTheArea(*self.guard):
            currPos = tuple(self.guard)
            if (currPos, currentDir) in visited:
                    return True
            else:
                posValue = self.input[self.guard[0]][self.guard[1]]

            if posValue == "#" or currPos == obstacle:
                self.guard[0] -= directions[currentDir][0]
                self.guard[1] -= directions[currentDir][1]
                currentDir = (currentDir + 1) % 4
            else:
                visited.add((currPos, currentDir))

            self.guard[0] += directions[currentDir][0]
            self.guard[1] += directions[currentDir][1]
        return False
