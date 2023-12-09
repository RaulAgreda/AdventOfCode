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
			inp = read_file("Inputs/input09.txt")
		else:
			inp, solutions = read_test("TestInputs/input09.txt")

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
	
	def predictNext(self, values:List[int]):
		nextValues = []
		allZero = True
		for v in range(len(values)-1):
			r = values[v+1] - values[v]
			if r != 0:
				allZero = False
			nextValues.append(r)
		if allZero:
			return values[-1]
		return values[-1] + self.predictNext(nextValues)

	def predictPrevious(self, values:List[int]):
		nextValues = []
		allZero = True
		for v in range(len(values)-1):
			r = values[v+1] - values[v]
			if r != 0:
				allZero = False
			nextValues.append(r)
		if allZero:
			return values[0]
		return values[0] - self.predictPrevious(nextValues)
	
	def part1(self):
		total = 0
		for line in self.inp:
			values = [int(x) for x in line.split()]
			total += self.predictNext(values)
		return total

	def part2(self):
		total = 0
		for line in self.inp:
			values = [int(x) for x in line.split()]
			total += self.predictPrevious(values)
		return total

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 09.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	