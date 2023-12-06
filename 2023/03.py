import sys
from utils.read_input import *

class Problem:
	def __init__(self, inp:str, part:str):
		self.inp = inp

		self.directions = [
			(1, 0),
			(0, 1),
			(-1, 0),
			(0, -1),
			(1, 1),
			(1, -1),
			(-1, 1),
			(-1, -1)
		]

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def getInputMatrix(self):
		matrix = []
		for line in self.inp:
			matrix.append(list(line))
		return matrix

	def checkSymbol(self, matrix, i, j):
		for dire in self.directions:
			idir = i + dire[0]
			jdir = j + dire[1]
			if 0 <= idir and idir < len(matrix) and 0 <= jdir and jdir < len(matrix[0]):
				char = matrix[idir][jdir]
				if  char != '.' and char.isdigit() == False:
					return True
		return False
	
	def checkGear(self, matrix, i, j):
		for dire in self.directions:
			idir = i + dire[0]
			jdir = j + dire[1]
			if 0 <= idir and idir < len(matrix) and 0 <= jdir and jdir < len(matrix[0]):
				if  matrix[idir][jdir] == '*':
					return (idir, jdir)
		return None
		

	def part1(self):
		total = 0
		matrix = self.getInputMatrix()
		for i in range(len(matrix)):
			currentNumber = ''
			addNumber = False
			for j in range(len(matrix[0])):
				if not matrix[i][j].isdigit():
					if addNumber:
						total += int(currentNumber)
					currentNumber = ''
					addNumber = False
				else:
					currentNumber += matrix[i][j]
					addNumber = addNumber or self.checkSymbol(matrix, i, j)
			if addNumber:
				total += int(currentNumber)
		return total

	def part2(self):
		matrix = self.getInputMatrix()
		gears = {}
		for i in range(len(matrix)):
			currentNumber = ''
			currentGear = None
			for j in range(len(matrix[0])):
				if not matrix[i][j].isdigit():
					if currentNumber != '' and currentGear is not None:
						gears[currentGear][-1] = int(currentNumber)
					currentNumber = ''
					currentGear = None
				else:
					currentNumber += matrix[i][j]
					gear = self.checkGear(matrix, i, j)
					if gear is not None:
						if gear not in gears:
							gears[gear] = [None]
						else:
							if gears[gear][-1] is not None:
								gears[gear].append(None)
						currentGear = gear
			if currentNumber != '' and currentGear is not None:
				gears[currentGear][-1] = int(currentNumber)
		total = 0
		for gear in gears:
			if len(gears[gear]) == 2:
				total += gears[gear][0] * gears[gear][1]
		return total

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 03.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input03.txt").split('\n')
	Problem(inp, sys.argv[1])
