import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		self.shape_score = { 
			"A": 1, "B": 2, "C": 3,
			"X": 1, "Y": 2, "Z": 3 }
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

	def win(self, x, y):
		"""Calculates the score if x wins y"""
		x = self.shape_score[x]
		y = self.shape_score[y]

		if x == 1 and y == 2:
			# Lose, rock loses to paper
			return x
		elif x == 1 and y == 3:
			# Win, rock beats scissors
			return x + 6
		elif x == 2 and y == 1:
			# Win, paper beats rock
			return x + 6
		elif x == 2 and y == 3:
			# Lose, paper loses to scissors
			return x
		elif x == 3 and y == 1:
			# Lose, scissors loses to rock
			return x
		elif x == 3 and y == 2:
			# Win, scissors beats paper
			return x + 6
		# Draw
		return x + 3

	def part1(self):
		score = 0
		for i in self.inp:
			guide = i.split(" ")
			score += self.win(guide[1], guide[0])
		return score

	def part2(self):
		win_dict = {
			"A": "B",
			"B": "C",
			"C": "A"
		}
		lose_dict = {
			"A": "C",
			"B": "A",
			"C": "B"
		}
		score = 0
		for i in self.inp:
			guide = i.split(" ")
			opponent = guide[0]
			strattegy = guide[1]
			if strattegy == "X":
				score += self.win(lose_dict[opponent], opponent)
			elif strattegy == "Y":
				score += self.win(opponent, opponent)
			else:
				score += self.win(win_dict[opponent], opponent)
		return score
			

if __name__ == "__main__":
	inp = read_file("Inputs/input02.txt").split("\n")[:-1]
	Problem(inp, sys.argv[1])


		
