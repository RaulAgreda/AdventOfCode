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
			inp = read_file("Inputs/input01.txt")
		else:
			inp, solutions = read_test("TestInputs/input01.txt")

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
	
	def read_input(self):
		left = []
		right = []
		for line in self.inp:
			l, r = line.split()
			left.append(int(l))
			right.append(int(r))
		return left, right
		
	def part1(self):
		left, right = self.read_input()
		left.sort()
		right.sort()
		total = 0
		for i in range(len(left)):
			total += abs(right[i] - left[i])
		return total

	def part2(self):
		left, right = self.read_input()
		similarity = {}
		# Initialize similarity score
		for l in left:
			similarity[l] = 0
		
		# Count the similarity for each number on the left
		for r in right:
			if r in similarity:
				similarity[r] += 1

		# Calculate the score
		total = 0
		for l in left:
			total += similarity[l] * l
		return total

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 01.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	