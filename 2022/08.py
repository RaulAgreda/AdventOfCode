import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

	def checkSides(self, start_i, start_j, M, visibles):
		i = start_i
		j = start_j
		directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
		for direction in directions:
			i = start_i
			j = start_j
			while (i >= 0 and j >= 0 and i < len(M) and j < len(M[0])):
				if i == 0 or j == 0 or i == len(M)-1 or j == len(M[0])-1:
					visibles[(start_i, start_j)] = M[start_i][start_j]
					return
				if M[i + direction[0]][j + direction[1]] >= M[start_i][start_j]:
					break
				i += direction[0]
				j += direction[1]
	
	def part1(self):
		self.visible = {}
		row_length = len(self.inp)
		col_length = len(self.inp[0])
		M = self.inp
		# check each row view
		for i in range(row_length):
			for j in range(col_length):
				self.checkSides(i, j, M, self.visible)
		return len(self.visible)

	def getSidesScores(self, start_i, start_j, M):
		total = 1
		tree_height = M[start_i][start_j]
		directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
		# print((start_i, start_j))
		for direction in directions:
			current_height = '0'
			trees_seen = 0
			i = start_i + direction[0]
			j = start_j + direction[1]
			while (i >= 0 and j >= 0 and i < len(M) and j < len(M[0])):
				trees_seen += 1
				if M[i][j] >= tree_height:
					break
				i += direction[0]
				j += direction[1]
			total *= trees_seen
			# print("\t", direction, trees_seen)
		# print(total)
		return total

	def part2(self):
		max_score = 0
		for i in range(1, len(self.inp) - 1):
			for j in range(1, len(self.inp[0]) - 1):	
				score = self.getSidesScores(i, j, self.inp)
				if score > max_score:
					max_score = score
		return max_score

if __name__ == "__main__":
	inp = read_file("Inputs/input08.txt").split('\n')
	Problem(inp, sys.argv[1])
