import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

compatibilities = {
	'|': ['n', 'w'],
	'-': ['e', 'w'],
	'L': ['n', 'e'],
	'J': ['n', 'w'],
	'7': ['s', 'w'],
	'F': ['s', 'e']
}

directions = ('u', 'd', 'l', 'r')
counterDir = {
	'u': 'd',
	'd': 'u',
	'l': 'r',
	'r': 'l'
}
directionsCoord = ((1, 0), (-1, 0), (0, -1), (0, 1))

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input10.txt")
		else:
			inp, solutions = read_test("TestInputs/input10.txt")

		self.inp = inp.split("\n")
		self.matrix = []
		for line in self.inp:
			self.matrix.append(line)
		self.connections = {
			"|": ['|', 'L']
		}
		
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
	
	def connectedTo(self, current, other:Literal['|', '-', 'L', 'J', '7', 'F'], otherPos:Literal['l', 'r', 'u', 'd']):
		"""@param: otherPos, position from this pipe"""
		if otherPos == 'u':
			return 'n' in compatibilities[current] and 's' in compatibilities[other]
		elif otherPos == 'd':
			return 's' in compatibilities[current] and 'n' in compatibilities[other]
		elif otherPos == 'l':
			return 'w' in compatibilities[current] and 'e' in compatibilities[other]
		else:
			return 'e' in compatibilities[current] and 'w' in compatibilities[other]

	def getStartPos(self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				if self.matrix[i][j] == 'S':
					return (i, j)
				
	def getLoop(self, pos, count, prevDir):
		print(self.matrix[pos[0]][pos[1]])
		for d in range(len(directions)):
			if directions[d] == counterDir[prevDir]:
				continue
			nPos = (pos[0] + directionsCoord[d][0], pos[1] + directionsCoord[d][1])
			if nPos[0] < 0 or nPos[0] >= len(self.matrix) or nPos[1] < 0 or nPos[1] >= len(self.matrix[0]):
				continue
			
			currentPipe = self.matrix[pos[0]][pos[1]]
			nextPipe = self.matrix[nPos[0]][nPos[1]]

			if nextPipe == '.':
				return -1
			if nextPipe == 'S':
				return count
			
			if not self.connectedTo(currentPipe, nextPipe, directions[d]):
				continue
			res = self.getLoop(nPos, count + 1, directions[d])
			if res != -1:
				return res
		return -1

				
	def part1(self):
		startPos = self.getStartPos()
		print(startPos)
		for d in range(len(directions)):
			nPos = (startPos[0] + directionsCoord[d][0], startPos[1] + directionsCoord[d][1])
			res = self.getLoop(nPos, 0, directions[d])
			if res != -1:
				return res

		

	def part2(self):
		pass

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 10.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	