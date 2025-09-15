from typing import *
from template.problem import Problem

class Day05(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        # super().__init__(input, part)
        first, second = input.split("\n\n")
        self.first_section = first.split("\n")
        self.second_section = second.split("\n")
        self.rules = {}
        for rule in self.first_section:
            key, value = rule.split("|")
            key = int(key)
            value = int(value)
            if key not in self.rules:
                self.rules[key] = [value]
            else:
                self.rules[key].append(value)
        self.solution = self.part1() if part == '1' else self.part2()
    
    def part1(self):
        """
        Implement the logic for part 1 of the problem.
        """
        total = 0
        for manual in self.second_section:
            numbers = [int(x) for x in manual.split(",")]
            if self.checkUpdate(numbers):
                # If the manual is valid, add the middle number to the result
                total += numbers[len(numbers) // 2]
        # Add your solution for part 1 here
        return total

    def part2(self):
        """
        Implement the logic for part 2 of the problem.
        """
        total = 0
        return total

    def checkUpdate(self, update):
        visited = set()
        for n in update:
            if n in self.rules:
                for v in self.rules[n]:
                    if v in visited:
                        # Is not valid
                        return False
            visited.add(n)
        return True
