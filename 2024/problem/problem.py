from typing import *

class Problem:
	'''
	@param input: The input text
	@param part: 1 or 2
	'''
	def __init__(self, input: str, part:str):
		self.inp = input.split("\n")
		self.solution = self.part1() if part == '1' else self.part2()
		
	def part1(self):
		return

	def part2(self):
		return

	def get_solution(self):
		return self.solution