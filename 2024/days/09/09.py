from typing import *
from template.problem import Problem

class Day09(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def part1(self):
        disk = [int(x) for x in list(self.input[0])]
        translation = []
        id = 0
        for i in range(0, len(disk), 2):
            a = 0
            for _ in range(disk[i]):
                translation.append(id)
            if i == len(disk) - 1:
                break
            for _ in range(disk[i+1]):
                translation.append(None)
            id+=1
        # Rearrange
        i = 0
        j = len(translation) - 1

        while i < j:
            while translation[j] is None:
                j-=1
            if translation[i] is None:
                translation[i], translation[j] = translation[j], translation[i]
                j -= 1
            i += 1
        i = 0
        total = 0
        while translation[i] is not None:
            total += i * translation[i]
            i+=1
        return total

    def part2(self):
        disk = [int(x) for x in list(self.input[0])]
        for i in range(0, len(disk), 2):
            pass
        return
