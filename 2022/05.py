import sys
from Inputs.ReadFile import *
import re

class CranesInput:
	def __init__(self, inp):
		self.inp = inp
		self.cranes_end_idx = 0
		for line in inp:
			if line[1] == '1':
				break
			self.cranes_end_idx += 1
		self.cranes = []
		for line in inp[:self.cranes_end_idx]:
			self.cranes.append(self.get_cranes(line))

	def get_cranes_piles(self):
		crane_columns = {}
		for j in range(len(self.cranes[0])):
			crane_columns[j+1] = []
			for i in range(len(self.cranes)):
				if self.cranes[i][j] != ' ':
					crane_columns[j+1].insert(0, self.cranes[i][j])
		return crane_columns

	def get_cranes(self, line):
		"""Returns a list of cranes from a line of input"""
		cranes = []
		state = 0
		i = 0
		while (i < len(line)):
			if state == 0:
				state = 1
			elif state == 1:
				cranes.append(line[i])
				i += 2
				state = 0
			i += 1
		return cranes

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		if self.inp[-1] == '':
			self.inp = self.inp[:-1]
		cranes_inp = CranesInput(self.inp)
		self.cranes = cranes_inp.get_cranes_piles()
		self.rules = self.get_rules(self.inp[cranes_inp.cranes_end_idx+2:])
		self.print_cranes()

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

	def print_cranes(self):
		for col in self.cranes:
			print(col, self.cranes[col])

	def get_rules(self, rules_input):
		rules = []
		for rule in rules_input:
			rules.append([int(x) for x in re.findall(r"\d+", rule)])
		return rules

	def return_result(self):
		result = ''
		for col in self.cranes:
			result += self.cranes[col][-1]
		return result

	def part1(self):
		for rule in self.rules:
			it, fr, to = rule
			for i in range(it):
				self.cranes[to].append(self.cranes[fr].pop())
		return self.return_result()

	def part2(self):
		for rule in self.rules:
			it, fr, to = rule
			# Add the cranes to the top of the pile
			self.cranes[to] += self.cranes[fr][-it:]
			# Remove the cranes added
			self.cranes[fr] = self.cranes[fr][:-it]
		return self.return_result()

if __name__ == "__main__":
	inp = read_file("Inputs/input05.txt").split('\n')
	Problem(inp, sys.argv[1])
