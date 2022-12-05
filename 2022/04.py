import sys
from Inputs.ReadFile import *

class SectionRange:
	def __init__(self, min, max):
		self.min = min
		self.max = max

	def overlap(self, other):
		return not (self.max < other.min or self.min > other.max)
		
	def __contains__(self, other):
		return self.min <= other.min and self.max >= other.max

	def __str__(self):
		return f"{self.min}-{self.max}"

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

	def part1(self):
		total = 0

		for line in self.inp:
			ranges = [x.split('-') for x in line.split(',')]
			ass1 = SectionRange(int(ranges[0][0]), int(ranges[0][1]))
			ass2 = SectionRange(int(ranges[1][0]), int(ranges[1][1]))
			if ass1 in ass2 or ass2 in ass1:
				total += 1
		return total

	def part2(self):
		total = 0

		for i in range(0, len(self.inp)):
			ranges = [x.split('-') for x in self.inp[i].split(',')]
			ass1 = SectionRange(int(ranges[0][0]), int(ranges[0][1]))
			ass2 = SectionRange(int(ranges[1][0]), int(ranges[1][1]))
			if ass1.overlap(ass2):
				total += 1
		return total

if __name__ == "__main__":
	inp = read_file("Inputs/input04.txt").split('\n')
	Problem(inp, sys.argv[1])
