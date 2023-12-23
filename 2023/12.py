import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *
# sys.setrecursionlimit(1000000)

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
		numbers_index: int = 0
		g_count: int = 0
		in_group: bool = False
		c: int = 0
		while c < len(pattern):
			if pattern[c] == '.':
				if in_group:
					if g_count != numbers[numbers_index]:
						return False
					numbers_index += 1
				g_count = 0
				in_group = False
			elif pattern[c] == '#':
				g_count += 1
				in_group = True
			else: # == ?
				return True
			if in_group:
				if g_count > numbers[numbers_index]:
					return False
			c+=1
		return int((not in_group) or in_group and g_count == numbers[numbers_index])

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
		n_groups = self.countGroups(pattern)
		if n_groups > len(numbers):
			return 0
		if not self.checkPatern(pattern, numbers):
			return 0
		if '?' not in pattern:
			return int(n_groups == len(numbers))
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
		total = 0
		for line in self.inp:
			pattern, numbers = line.split()
			numbers = [int(x) for x in numbers.split(',')]
			original = pattern
			for _ in range(4):
				pattern += '?'
				pattern += original
			print(pattern)
			total += self.getCombinations(pattern, numbers)
		return total

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 12.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	