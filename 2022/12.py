import sys
from Inputs.ReadFile import *
from collections import deque

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		self.d = {a: ord(a) - 96 for a in 'abcdefghijklmnopqrstuvwxyz'}
		self.d['S'] = 1
		self.d['E'] = 26
		self.nodes = {}
		self.heur = {}
		self.Start, self.End = self.get_start_end_nodes()
		for i in range(len(self.inp)):
			for j in range(len(self.inp[0])):
				self.nodes[(i, j)] = self.d[self.inp[i][j]]
				self.heur[(i, j)] = abs(self.End[0] - i) + abs(self.End[1] - j)
		self.dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def get_start_end_nodes(self):
		for i in range(len(self.inp)):
			for j in range(len(self.inp[0])):
				if self.inp[i][j] == 'S':
					Start = (i, j)
				elif self.inp[i][j] == 'E':
					End = (i, j)
		return Start, End

	def bfs(self, Start, End):
		q = deque()
		q.append([Start])
		visited = set()
		while q:
			path = q.popleft()
			node = path[-1]
			if node in visited:
				continue
			if node == End:
				return len(path) - 1
			visited.add(node)
			for d in self.dirs:
				child = (node[0] + d[0], node[1] + d[1])
				if  0 <= child[0] < len(self.inp) and 0 <= child[1] < len(self.inp[0]):
					if self.nodes[child] - self.nodes[node] <= 1:
						path_copy = path[:]
						path_copy.append(child)
						q.append(path_copy)
		return -1


	def part1(self):
		return self.bfs(self.Start, self.End)

	def part2(self):
		Start = self.Start
		min = 999999
		for i in range(len(self.inp)):
			for j in range(len(self.inp[0])):
				if self.inp[i][j] == 'a':
					Start = (i, j)
					current = self.bfs(Start, self.End)
					if current > 0 and current < min:
						min = current
		return min

if __name__ == "__main__":
	inp = read_file("Inputs/input12.txt").split('\n')
	Problem(inp, sys.argv[1])
