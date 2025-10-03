from typing import *
from template.problem import Problem
import time

class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Day15(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        # super().__init__(input, part)
        self.input = input.split('\n\n')
        self.map = [list(line) for line in self.input[0].split('\n')]
        self.moves = self.input[1].replace('\n', '')
        self.solution = self.part1() if part == '1' else self.part2()

    def moveObstacle(self, i, j, dir):
        if self.map[i+dir[0]][j+dir[1]] == '.':
            self.map[i][j], self.map[i+dir[0]][j+dir[1]] = self.map[i+dir[0]][j+dir[1]], self.map[i][j]
            return True
        if self.map[i+dir[0]][j+dir[1]] == '#':
            return False
        if self.moveObstacle(i+dir[0], j+dir[1], dir):
            self.map[i][j], self.map[i+dir[0]][j+dir[1]] = self.map[i+dir[0]][j+dir[1]], self.map[i][j]
            return True

    def printMap(self, map):
        for line in map:
            print(''.join(line))
        print()

    def part1(self):
        dirs = {
            "^": (-1, 0),
            "<": (0, -1),
            ">": (0, 1),
            "v": (1, 0)
        }
        robot = None
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == '@':
                    robot = [i, j]

        for move in self.moves:
            dir = dirs[move]
            nextPos = robot[0]+dir[0], robot[1]+dir[1]
            nextV = self.map[nextPos[0]][nextPos[1]]
            if nextV == '.':
                self.map[robot[0]][robot[1]] = '.'
                self.map[nextPos[0]][nextPos[1]] = '@'
                robot[0] = nextPos[0]
                robot[1] = nextPos[1]
            elif nextV == 'O':
                if self.moveObstacle(robot[0], robot[1], dir):
                    robot[0] = nextPos[0]
                    robot[1] = nextPos[1]
            # self.printMap(self.map) # animate :)
            # time.sleep(0.25)
        
        total = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 'O':
                    total += i * 100 + j

        return total

    def getNewMap(self):
        newMap = []
        for line in self.map:
            newLine = []
            for c in line:
                if c == '@':
                    newLine.append('@')
                    newLine.append('.')
                elif c == 'O':
                    newLine.append('[')
                    newLine.append(']')
                else:
                    newLine.append(c)
                    newLine.append(c)
            newMap.append(newLine)
        return newMap
    
    def moveObstacleHorizontal(self, i, j, dir, map):
        if map[i+dir[0]][j+dir[1]] == '.':
            map[i][j], map[i+dir[0]][j+dir[1]] = map[i+dir[0]][j+dir[1]], map[i][j]
            return True
        if map[i+dir[0]][j+dir[1]] == '#':
            return False
        if self.moveObstacleHorizontal(i+dir[0], j+dir[1], dir, map):
            map[i][j], map[i+dir[0]][j+dir[1]] = map[i+dir[0]][j+dir[1]], map[i][j]
            return True

    def moveObstacleVertical(self, i, j, dir, map):
        if map[i+dir[0]][j+dir[1]] == '.':
            if map[i][j] == '[' and map[i+dir[0]][j+dir[1]+1] == '#':
                return False
            if map[i][j] == ']' and map[i+dir[0]][j+dir[1]-1] == '#':
                return False
            # Move the box
            map[i][j], map[i+dir[0]][j+dir[1]] = map[i+dir[0]][j+dir[1]], map[i][j]
            if map[i][j] == '[':
                map[i][j], map[i+dir[0]][j+dir[1]+1] = map[i+dir[0]][j+dir[1]+1], map[i][j]
            elif map[i][j] == ']':
                map[i][j], map[i+dir[0]][j+dir[1]-1] = map[i+dir[0]][j+dir[1]-1], map[i][j]
            return True
        if map[i+dir[0]][j+dir[1]] == '#':
            return False
        if self.moveObstacleVertical(i+dir[0], j+dir[1], dir, map):
            map[i][j], map[i+dir[0]][j+dir[1]] = map[i+dir[0]][j+dir[1]], map[i][j]
            if map[i][j] == '[':
                map[i][j], map[i+dir[0]][j+dir[1]+1] = map[i+dir[0]][j+dir[1]+1], map[i][j]
            elif map[i][j] == ']':
                map[i][j], map[i+dir[0]][j+dir[1]-1] = map[i+dir[0]][j+dir[1]-1], map[i][j]
            return True

    def part2(self):
        newMap = self.getNewMap()
        self.printMap(newMap)       
        
        dirs = {
            "^": (-1, 0),
            "<": (0, -1),
            ">": (0, 1),
            "v": (1, 0)
        }
        robot = None
        for i in range(len(newMap)):
            for j in range(len(newMap[0])):
                if newMap[i][j] == '@':
                    robot = [i, j]
        for move in self.moves:
            dir = dirs[move]
            nextPos = robot[0]+dir[0], robot[1]+dir[1]
            nextV = newMap[nextPos[0]][nextPos[1]]
            if nextV == '.':
                newMap[robot[0]][robot[1]] = '.'
                newMap[nextPos[0]][nextPos[1]] = '@'
                robot[0] = nextPos[0]
                robot[1] = nextPos[1]
            elif nextV in '[]':
                moveRobot = False
                if move in "<>":
                    # Horizontally is the same as before
                    if self.moveObstacleHorizontal(robot[0], robot[1], dir, newMap):
                        moveRobot = True
                else:
                    if self.moveObstacleVertical(nextPos[0], nextPos[1], dir, newMap):
                        moveRobot = True
                
                if moveRobot:
                    newMap[robot[0]][robot[1]] = '.'
                    newMap[nextPos[0]][nextPos[1]] = '@'
                    robot[0] = nextPos[0]
                    robot[1] = nextPos[1]
            self.printMap(newMap)       

        return
