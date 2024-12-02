from typing import *
from problem.problem import Problem

class Day02(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def isSafe(self, nums):
        decreasing = nums[1] < nums[0]

        for i in range(len(nums) - 1):
            areDecreasing = nums[i+1] < nums[i]
            if areDecreasing != decreasing:
                return False, i + 1
            
            differ = abs(nums[i+1] - nums[i])

            if differ == 0 or differ > 3:
                return False, i + 1
        return True, -1

    def part1(self):
        safe_count = 0
        for line in self.input:
            nums = [int(x) for x in line.split()]
            if self.isSafe(nums)[0]:
                safe_count+=1
        return safe_count

    def part2(self):
        safe_count = 0
        for line in self.input:
            nums = [int(x) for x in line.split()]
            isSafe, problemIdx = self.isSafe(nums)
            
            if isSafe:
                safe_count+=1
                continue

            try1 = nums.copy()
            try2 = nums.copy()
            try3 = nums.copy()
            # Three cases to check, removing the current element that differs, the next element that differs, and the first element
            del try1[problemIdx]
            del try2[0]
            del try3[problemIdx - 1]

            isSafe = self.isSafe(try1)[0] or self.isSafe(try2)[0] or self.isSafe(try3)[0]

            if isSafe:
                safe_count+=1

        return safe_count
