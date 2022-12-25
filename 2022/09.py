import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		self.rules = [(x.split()[0], int(x.split()[1])) for x in self.inp]
		self.directions = {
			'L': (-1, 0),
			'R': (1, 0),
			'U': (0, 1),
			'D': (0, -1)
		}
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def part1(self):
		h_pos = [0, 0]
		t_pos = [0, 0]
		visited = set()
		for rule in self.rules:
			direction = self.directions[rule[0]]
			repeat = rule[1]
			for i in range(repeat):
				h_pos[0] += direction[0]
				h_pos[1] += direction[1]
				if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
					t_pos[0] = h_pos[0] - direction[0]
					t_pos[1] = h_pos[1] - direction[1]
				visited.add(tuple(t_pos))
		return len(visited)

	def sign(self, x):
		if x < 0:
			return -1
		if x > 0:
			return 1
		return 0

	def part2(self):
		rope = ()
		for i in range(10):
			rope += ([0, 0],)
		visited = set()
		for rule in self.rules:
			print(rule)
			direction = self.directions[rule[0]]
			repeat = rule[1]
			for i in range(repeat):
				rope[0][0] += direction[0]
				rope[0][1] += direction[1]
				for i in range(len(rope)-1):
					diff_x = rope[i][0] - rope[i+1][0]
					diff_y = rope[i][1] - rope[i+1][1]
					if (abs(diff_x) > 1 or abs(diff_y) > 1):
						rope[i+1][0] += self.sign(diff_x)
						rope[i+1][1] += self.sign(diff_y)
				visited.add(tuple(rope[-1]))
				print(rope)
		return len(visited)

if __name__ == "__main__":
	inp = read_file("Inputs/input09.txt").split('\n')
	Problem(inp, sys.argv[1])
