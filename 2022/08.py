import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def part1(self):
		visible = set()
		row_length = len(self.inp)
		col_length = len(self.inp[0])
		M = self.inp
		# check each row view
		for i in range(row_length):
			for j in range(col_length):
				self.checkSides(i, j, M, visible)
		# print(visible)
		return len(visible)

	def checkSides(self, start_i, start_j, M, visibles):
		i = start_i
		j = start_j
		if i == 0 or j == 0 or i == len(M)-1 or j == len(M[0])-1:
			visibles.add((i,j))
			return
		# Check left
		while (j >= 0):
			if j == 0 or (i, j) in visibles:
				visibles.add((start_i, start_j))
				return
			if M[i][j] <= M[i][j-1]:
				break
			j -= 1
		# Check right
		j = start_j
		while (j < len(M[0])):
			if j == len(M[0])-1 or (i, j) in visibles:
				visibles.add((start_i, start_j))
				return
			if M[i][j] <= M[i][j+1]:
				break
			j += 1
		# Check up
		j = start_j
		while (i >= 0):
			if i == 0 or (i, j) in visibles:
				visibles.add((start_i, start_j))
				return
			if M[i][j] <= M[i-1][j]:
				break
			i -= 1
		# Check down
		i = start_i
		while (i < len(M)):
			if i == len(M)-1 or (i, j) in visibles:
				visibles.add((start_i, start_j))
				return
			if M[i][j] <= M[i+1][j]:
				break
			i += 1

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input08.txt").split('\n')
	Problem(inp, sys.argv[1])
