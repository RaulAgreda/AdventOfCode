from typing import *
from template.problem import Problem

class Day07(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def test_ecuation(self, numbers:list, result):
        if len(numbers) == 1:
            return numbers[0] == result
        
        addOp = numbers[0] + numbers[1]
        addN = numbers.copy()
        addN.pop(0)
        addN[0] = addOp
        mulOp = numbers[0] * numbers[1]
        mulN = addN.copy()
        mulN[0] = mulOp
        return self.test_ecuation(addN, result) or self.test_ecuation(mulN, result)
    
    def test_ecuation2(self, numbers:list, result):
        if len(numbers) == 1:
            return numbers[0] == result
        
        addOp = numbers[0] + numbers[1]
        addN = numbers.copy()
        addN.pop(0)
        addN[0] = addOp
        mulOp = numbers[0] * numbers[1]
        mulN = addN.copy()
        mulN[0] = mulOp
        orOp = int(str(numbers[0]) + str(numbers[1]))
        orN = mulN.copy()
        orN[0] = orOp
        return self.test_ecuation2(addN, result) or self.test_ecuation2(mulN, result) or self.test_ecuation2(orN, result)

    def part1(self):
        total = 0
        for line in self.input:
            result, numbers = line.split(": ")
            result = int(result)
            numbers = [int(x) for x in numbers.split()]
            if self.test_ecuation(numbers, result):
                total += result

        return total

    def part2(self):
        total = 0
        for line in self.input:
            result, numbers = line.split(": ")
            result = int(result)
            numbers = [int(x) for x in numbers.split()]
            if self.test_ecuation2(numbers, result):
                total += result

        return total
