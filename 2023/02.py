import sys
from utils.read_input import *

class Problem:
	def __init__(self, inp:str, part:str):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def parseInput(self):
		data = {}
		i = 1
		for line in self.inp:
			gameInfo = line.split(": ")[1]
			data[i] = []
			sets = gameInfo.split("; ")
			for set in sets:
				data[i].append(self.parseSet(set))
			i+=1
		return data

	def parseSet(self, set):
		"""Gets input with format '<number> color, <number> color,...
		and returns a dictionary with the number of each color"""
		cubes = set.split(",")
		ret = {
			"red": 0,
			"blue": 0,
			"green": 0
		}
		for n_color in cubes:
			data = n_color.split()
			n = int(data[0])
			col = data[1]
			ret[col] = n
		return ret

	def part1(self):
		MAX = {
			"red": 12,
			"green": 13,
			"blue": 14
		}

		validGames = set(range(1, len(self.inp) + 1))
		data = self.parseInput()
		for game in data:
			for game_set in data[game]:
				for color in game_set:
					if game_set[color] > MAX[color]:
						if game in validGames:
							validGames.remove(game)
						break
		return sum(validGames)


	def part2(self):
		data = self.parseInput()
		total = 0
		for game in data:
			maxCubes = {
				"red": 0,
				"green": 0,
				"blue": 0
			}
			for game_set in data[game]:
				for color in game_set:
					maxCubes[color] = max(maxCubes[color], game_set[color])
			power = 1
			for color in maxCubes:
				power *= maxCubes[color]
			total += power
		return total
			

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 02.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input02.txt").split('\n')
	Problem(inp, sys.argv[1])
