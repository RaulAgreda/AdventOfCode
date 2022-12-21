import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def checkAllDifferent(self, substr):
		seen = set()
		for c in substr:
			if c in seen:
				return False
			seen.add(c)
		return True

	def part1(self):
		for i in range(len(self.inp)):
			if (self.checkAllDifferent(self.inp[i:i+4])):
				return i + 4

	def part2(self):
		for i in range(len(self.inp)-14):
			if (self.checkAllDifferent(self.inp[i:i+14])):
				return i + 14

if __name__ == "__main__":
	inp = read_file("Inputs/input06.txt")
	Problem(inp, sys.argv[1])
