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
		cycle = 1
		X = 1
		# [Cycle, value]
		next_X = [0, 1]
		total = 0
		next_add = 20
		for instruction in self.inp:
			ins = instruction.split(' ')
			if cycle >= next_add:
				if next_add >= next_X[0]:
					X = next_X[1]
				# print(cycle, next_add, X, next_X)
				total += X * next_add
				next_add += 40
			if cycle >= next_X[0]:
				X = next_X[1]
			if ins[0] == 'addx':
				cycle += 2
				next_X[0] = cycle
				next_X[1] = X + int(ins[1])
			else:
				cycle += 1
		return total

	def CRT(self):
		cycle = 1
		next_inst = 0
		next_inst_cycle = 1
		X = 1
		# [Cycle, value]
		next_X = [1, 1]
		while True:
			if cycle == next_X[0]:
				X = next_X[1]
			if cycle == next_inst_cycle:
				if next_inst >= len(self.inp):
					break
				ins = self.inp[next_inst].split(' ')
				next_inst += 1
				if ins[0] == 'addx':
					next_inst_cycle += 2
					next_X[0] = next_inst_cycle
					next_X[1] = X + int(ins[1])
				else:
					next_inst_cycle += 1
			draw_pixel = (cycle - 1) % 40
			if draw_pixel == X - 1 or draw_pixel == X or draw_pixel == X + 1:
				print('#', end='')
			else:
				print('.', end='')
			if cycle % 40 == 0:
				print()
			cycle += 1
		

	def part2(self):
		self.CRT()

if __name__ == "__main__":
	inp = read_file("Inputs/input10.txt").split('\n')
	Problem(inp, sys.argv[1])
