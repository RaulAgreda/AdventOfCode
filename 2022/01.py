import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def total_elfs_calories(self):
		total_calories = []
		for elf in inp:
			elf_calories = []
			for x in elf.split("\n"):
				if x != "":
					elf_calories.append(int(x))
			total_calories.append(sum(elf_calories))
		return total_calories

	def part1(self):
		return max(self.total_elfs_calories())

	def part2(self):
		total_calories = self.total_elfs_calories()
		total_calories.sort()
		return sum(total_calories[-3:])


if __name__ == "__main__":
	inp = read_file("Inputs/input01.txt").split('\n\n')
	Problem(inp, sys.argv[1])
