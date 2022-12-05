import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

	def type_value(self, x: chr):
		if 'a' <= x <= 'z':
			return ord(x) - ord('a') + 1
		return ord(x) - ord('A') + 27

	def part1(self):
		# I'm not proud of this solution, but it works
		total = 0

		for line in self.inp:
			part1 = set(line[:len(line)//2])
			part2 = set(line[len(line)//2:])
			a = list(part1 & part2)[0]
			total += self.type_value(a)
		return total


	def part2(self):
		total = 0

		for i in range(0, len(self.inp), 3):
			elf1 = self.inp[i]
			elf2 = self.inp[i+1]
			elf3 = self.inp[i+2]
			a = list(set(elf1) & set(elf2) & set(elf3))[0]
			total += self.type_value(a)
		return total



if __name__ == "__main__":
	inp = read_file("Inputs/input03.txt").split('\n')
	Problem(inp, sys.argv[1])
