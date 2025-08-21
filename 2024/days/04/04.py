from typing import *
from template.problem import Problem

class Day04(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def part1(self):
        result = 0
        directions = [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,1), (1,-1), (-1,-1)]
        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                if (self.input[i][j] == 'X'):
                    for dir in directions:
                        word = ""
                        for d in range(4):
                            i2 = i + d * dir[0]
                            j2 = j + d * dir[1]
                            if 0 <= i2 and i2 < len(self.input) and 0 <= j2 and j2 < len(self.input[0]):
                                word += self.input[i2][j2]
                        if word == "XMAS":
                            result += 1
        return result

    def part2(self):
        result = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[i])):
                if (self.input[i][j] == 'A'):
                    if 0 < i and i < len(self.input) - 1 and 0 < j and j < len(self.input[0]) - 1:
                        word = self.input[i-1][j-1] + "A" + self.input[i+1][j+1]
                        if word == "SAM" or word == "MAS":
                            word = self.input[i-1][j+1] + "A" + self.input[i+1][j-1]
                            if word == "SAM" or word == "MAS":
                                result += 1
        return result
