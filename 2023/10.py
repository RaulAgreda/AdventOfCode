import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *
import copy

sys.setrecursionlimit(1000000)

compatibilities = {
	'|': ['n', 's'],
	'-': ['e', 'w'],
	'L': ['n', 'e'],
	'J': ['n', 'w'],
	'7': ['s', 'w'],
	'F': ['s', 'e']
}

directions = ('n', 's', 'w', 'e')
counterDir = {
	'n': 's',
	's': 'n',
	'w': 'e',
	'e': 'w'
}
directionsCoord = ((-1, 0), (1, 0), (0, -1), (0, 1))

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
	
	def connectedTo(self, current, other:Literal['|', '-', 'L', 'J', '7', 'F'], otherPos:Literal['w', 'e', 'n', 's']):
		"""@param: otherPos, position from this pipe"""
		if otherPos == 'n':
			return 'n' in compatibilities[current] and 's' in compatibilities[other]
		elif otherPos == 's':
			return 's' in compatibilities[current] and 'n' in compatibilities[other]
		elif otherPos == 'w':
			return 'w' in compatibilities[current] and 'e' in compatibilities[other]
		else:
			return 'e' in compatibilities[current] and 'w' in compatibilities[other]

	def getStartPos(self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				if self.matrix[i][j] == 'S':
					return (i, j)
				
	def getLoopCount(self, pos, count, prevDir):
		currentPipe = self.matrix[pos[0]][pos[1]]
		if currentPipe == '.':
			return -1
		for d in range(len(directions)):
			if directions[d] == counterDir[prevDir]:
				continue
			if directions[d] not in compatibilities[currentPipe]:
				continue
			nPos = (pos[0] + directionsCoord[d][0], pos[1] + directionsCoord[d][1])
			if nPos[0] < 0 or nPos[0] >= len(self.matrix) or nPos[1] < 0 or nPos[1] >= len(self.matrix[0]):
				continue
			
			nextPipe = self.matrix[nPos[0]][nPos[1]]
			if nextPipe == 'S':
				return count
			if nextPipe == '.':
				continue
			if not self.connectedTo(currentPipe, nextPipe, directions[d]):
				continue
			res = self.getLoopCount(nPos, count + 1, directions[d])
			if res != -1:
				return res
		return -1
				
	def part1(self):
		startPos = self.getStartPos()
		for d in range(len(directions)):
			nPos = (startPos[0] + directionsCoord[d][0], startPos[1] + directionsCoord[d][1])
			nextPipe = self.matrix[nPos[0]][nPos[1]]
			if nextPipe == '.':
				continue
			if counterDir[directions[d]] in compatibilities[nextPipe]:
				res = self.getLoopCount(nPos, 0, directions[d])
				if res != -1:
					return res // 2 + 1

	def clearMatrix(self, startPos):
		m = []
		for i in range(len(self.matrix)):
			m.append([])
			for j in range(len(self.matrix[0])):
				if (i, j) == startPos:
					m[i].append('S')
				m[i].append('.')
		return m

	def getLoop(self, pos, loopMatrix, prevDir):
		currentPipe = self.matrix[pos[0]][pos[1]]
		if currentPipe == '.':
			return -1
		for d in range(len(directions)):
			if directions[d] == counterDir[prevDir]:
				continue
			if directions[d] not in compatibilities[currentPipe]:
				continue
			nPos = (pos[0] + directionsCoord[d][0], pos[1] + directionsCoord[d][1])
			if nPos[0] < 0 or nPos[0] >= len(self.matrix) or nPos[1] < 0 or nPos[1] >= len(self.matrix[0]):
				continue
			
			nextPipe = self.matrix[nPos[0]][nPos[1]]
			if nextPipe == 'S':
				loopMatrix[pos[0]][pos[1]] = currentPipe
				return loopMatrix
			if nextPipe == '.':
				continue
			if not self.connectedTo(currentPipe, nextPipe, directions[d]):
				continue
			res = self.getLoop(nPos, loopMatrix, directions[d])
			if res is not None:
				loopMatrix[pos[0]][pos[1]] = currentPipe
				return loopMatrix
		return None
	
	def getStartPipeType(self, startPos, matrix):
		dirs = []
		for d in range(len(directions)):
			checkPos = (startPos[0] + directionsCoord[d][0], startPos[1] + directionsCoord[d][1])
			if checkPos[0] < 0 or checkPos[0] >= len(matrix) or checkPos[1] < 0 or checkPos[1] >= len(matrix[0]):
				continue
			checkPipe = matrix[checkPos[0]][checkPos[1]]
			if checkPipe == '.':
				continue
			for type in compatibilities:
				if self.connectedTo(type, checkPipe, directions[d]):
					dirs.append(directions[d])
		for type in compatibilities:
			if dirs[0] in compatibilities[type] and dirs[1] in compatibilities[type]:
				return type

	def part2(self):
		startPos = self.getStartPos()
		loopMatrix = self.clearMatrix(startPos)
		# Like part 1
		for d in range(len(directions)):
			nPos = (startPos[0] + directionsCoord[d][0], startPos[1] + directionsCoord[d][1])
			nextPipe = self.matrix[nPos[0]][nPos[1]]
			if nextPipe == '.':
				continue
			if counterDir[directions[d]] in compatibilities[nextPipe]:
				loopMatrix = self.clearMatrix(startPos)
				res = self.getLoop(nPos, loopMatrix, directions[d])
				if res != -1:
					break
		# The S messes with the mathematic algorithm so we replace it for it's corresponding pipe
		loopMatrix[startPos[0]][startPos[1]] = self.getStartPipeType(startPos, loopMatrix)
		# Yes, I'm going to make this visual because it's cool
		total = 0
		visualMatrix = copy.deepcopy(loopMatrix)
		# To know if the empty '.' is inside or outside the loop, we count the loop edges, if it is odd, it is inside, else it is not
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				if loopMatrix[i][j] == '.':
					odd = False
					j2 = j+1
					while j2 < len(self.matrix[0]):
						if loopMatrix[i][j2] == '|':
							odd = not odd
						# Here we take in count as odd L -* 7 or F -* J
						elif loopMatrix[i][j2] == 'L':
							while loopMatrix[i][j2+1] == '-':
								j2+=1
							if loopMatrix[i][j2+1] == '7':
								odd = not odd
						elif loopMatrix[i][j2] == 'F':
							while loopMatrix[i][j2+1] == '-':
								j2+=1
							if loopMatrix[i][j2+1] == 'J':
								odd = not odd
						j2+=1								
					if odd:
						total += 1
						visualMatrix[i][j] = "X"
		for l in visualMatrix:
			for c in l:
				if c == 'X':
					print("\033[92mX\033[0m", end='')
				else:
					print(c, end='')
			print()
		return total

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 10.py 1|2 [-t]")
		print("1: run part 1\n2: run part 2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	