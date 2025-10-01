from typing import *
from template.problem import Problem
import math

class Day11(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def getDigits(self, val):
        if val == 0:
            return 1
        return int(math.log10(val)) + 1

    def blink(self, val, it, maxIt, knownStones: set):
        key = (val, it)
        if key in knownStones:
            return knownStones[key]
        if it == maxIt:
            return 1
        if val == 0:
            divisions = self.blink(1, it+1, maxIt, knownStones)
        else:
            n = self.getDigits(val)
            if n % 2 == 0:
                fact = 10 ** (n//2)
                a, b = val // fact, val % fact
                divisions = self.blink(a, it+1, maxIt, knownStones) + self.blink(b, it+1, maxIt, knownStones)
            else:
                divisions = self.blink(val*2024, it +1, maxIt, knownStones)
        knownStones[key] = divisions
        return divisions
            
    def part1(self, maxIt = 25):
        startStones = [int(x) for x in self.input[0].split()]
        total = 0
        for stone in startStones:
            total += self.blink(stone, 0, maxIt, {})
        return total

    def part2(self):
        return self.part1(75)
