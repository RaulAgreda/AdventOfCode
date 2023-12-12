import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input12.txt")
		else:
			inp, solutions = read_test("TestInputs/input12.txt")

		self.inp = inp.split("\n")
		
		result = self.part1() if part == '1' else self.part2()
		if not test:
			print(result)
		else:
			solution = solutions[0] if part == '1' else solutions[1]
			self.do_unit_test(str(result), solution)

	def do_unit_test(self, result:str, solution:str):
		if result == solution:
			print(f"{Colors.GREEN}[OK] {Colors.RESET}The example result is correct!!")
		else:
			print(f"{Colors.RED}[ERROR] {Colors.RESET}The example result is wrong!!")
			print(f"{Colors.YELLOW}Expected: {Colors.RESET}{solution}")
			print(f"{Colors.YELLOW}Got: {Colors.RESET}{result}")
	
	def checkPatern(self, pattern:str, numbers:List[int]):
		if (self.countGroups(pattern) != len(numbers)):
			return False
		groupCount = 0
		groupIdx = 0
		inGroup = pattern[0] == '#'
		for c in pattern:
			if c == '.':
				if inGroup:
					if groupCount != numbers[groupIdx]:
						return False
					groupIdx += 1
				groupCount = 0
				inGroup = False
			elif c == '#':
				inGroup = True
				groupCount+=1
			elif c == '?':
				break
		if inGroup:
			if groupCount != numbers[groupIdx]:
				return False
			groupIdx += 1
		return True

	def countGroups(self, pattern):
		count = 0
		inGroup = False
		for c in pattern:
			if c == '#':
				if not inGroup:
					count += 1
				inGroup = True
			elif c == '.':
				inGroup = False
			elif c == '?':
				return count
		return count

	def getCombinations(self, pattern:str, numbers:List[int]):
		if '?' not in pattern:
			return int(self.checkPatern(pattern, numbers))
		if self.countGroups(pattern) > len(numbers):
			return 0
		p1 = self.getCombinations(pattern.replace('?', '#', 1), numbers)
		p2 = self.getCombinations(pattern.replace('?', '.', 1), numbers)
		return p1 + p2
		

	def part1(self):
		total = 0
		for line in self.inp:
			pattern, numbers = line.split()
			numbers = [int(x) for x in numbers.split(',')]
			total += self.getCombinations(pattern, numbers)
		return total


	def part2(self):
		print(self.countGroups("#...####.####"))
		print(self.countGroups("#...####.####.###."))
		print(self.countGroups("..#...####.####.###."))
		print(self.countGroups("..#......."))
		print(self.countGroups("........"))
		pass

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 12.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	