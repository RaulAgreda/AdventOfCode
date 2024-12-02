from typing import *
from template.problem import Problem

class Day01(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def read_input(self):
        left = []
        right = []
        for line in self.inp:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
        return left, right

    def part1(self):
        left, right = self.read_input()
        left.sort()
        right.sort()
        total = 0
        for i in range(len(left)):
            total += abs(right[i] - left[i])
        return total

    def part2(self):
        left, right = self.read_input()
        similarity = {}
        # Initialize similarity score
        for l in left:
            similarity[l] = 0

        # Count the similarity for each number on the left
        for r in right:
            if r in similarity:
                similarity[r] += 1

        # Calculate the score
        total = 0
        for l in left:
            total += similarity[l] * l
        return total
