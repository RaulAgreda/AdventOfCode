import sys
from Inputs.ReadFile import *
import queue

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		self.d = {a: ord(a) - 96 for a in 'abcdefghijklmnopqrstuvwxyz'}
		self.d['S'] = 1
		self.d['E'] = 26
		self.dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def create_nodes(self):
		Start = None
		End = None
		for i in range(len(self.inp)):
			for j in range(len(self.inp[0])):
				if self.inp[i][j] == 'S':
					Start = (i, j)
				elif self.inp[i][j] == 'E':
					End = (i, j)
		return Start, End

	def bfs(self, Start, End):
		q = deque()
		q.put(Start)
		visited = set()
		visited.add(Start.id)
		while not q.empty():
			current = q.get()
			if current == End:
				return True
			for node in current.posib:
				if node.id not in visited:
					q.put(node)
					visited.add(node.id)
		return False

	def part1(self):
		Start, End = self.create_nodes()
		return self.bfs(Start, End)

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input12.txt").split('\n')
	Problem(inp, sys.argv[1])
