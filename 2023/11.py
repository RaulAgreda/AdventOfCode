import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

class Vector2:
	def __init__(self, i, j):
		self.i = i
		self.j = j

	def distance(self, other:'Vector2'):
		"""Manhatan distance"""
		return abs(other.i - self.i) + abs(other.j - self.j)
	
	def __str__(self):
		return f"({self.i}, {self.j})"
	
	def copy(self)->'Vector2':
		return Vector2(self.i, self.j)

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input11.txt")
		else:
			inp, solutions = read_test("TestInputs/input11.txt")

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

	def getStars(self, expansion=1)->List[Vector2]:
		stars = []
		emptyRows = set([i for i in range(len(self.inp))])
		emptyCols = set([j for j in range(len(self.inp[0]))])
		# we add the initial stars coord, and in the meantime record what rows and columns are empty
		for i in range(len(self.inp)):
			for j in range(len(self.inp[0])):
				if (self.inp[i][j] == '#'):
					newStar = Vector2(i, j)
					stars.append(newStar)
					if i in emptyRows:
						emptyRows.remove(i)
					if j in emptyCols:
						emptyCols.remove(j)

		startStars = []
		for star in stars:
			startStars.append(star.copy())
		for empRow in emptyRows:
			for s in range(len(stars)):
				if startStars[s].i > empRow:
					stars[s].i += expansion
		for empCol in emptyCols:
			for s in range(len(stars)):
				if startStars[s].j > empCol:
					stars[s].j += expansion
		return stars
		# now we check the space between galaxies and add them
	
	def part1(self, expansion=1):
		stars = self.getStars(expansion)
		total = 0
		for s1 in range(len(stars)-1):
			for s2 in range(s1+1, len(stars)):
					total += stars[s1].distance(stars[s2])
		return total
	
	def part2(self):
		return self.part1(999999)


if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 11.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	