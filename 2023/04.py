import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp:str, part:str):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def parseInput(self):
		games = []
		game = {
			"win": [],
			"yours": []
		}
		for line in self.inp:
			data = line.split(": ")[1]
			win, yours = data.split(" | ")
			currentGame = game.copy()
			currentGame["win"] = [int(x) for x in win.split()]
			currentGame["yours"] = [int(x) for x in yours.split()]
			games.append(currentGame)

		return games


	def part1(self):
		total = 0
		games = self.parseInput()
		for game in games:
			currentGame = 0
			for card in game["yours"]:
				if card in game["win"]:
					if currentGame == 0:
						currentGame = 1
					else:
						currentGame *= 2
			total += currentGame
		return total

	def part2(self):
		scratchCards = {}
		games = self.parseInput()
		for g in range(len(games)):
			scratchCards[g+1] = 1
		for g in range(len(games)):
			# currentGame: g+1
			nWin = 0
			for card in games[g]["yours"]:
				if card in games[g]["win"]:
					nWin += 1
			#nextGame: g+2
			for i in range(nWin):
				scratchCards[g+2+i] += scratchCards[g+1]
		total = 0
		for k in scratchCards:
			total += scratchCards[k]
		return total
if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 04.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input04.txt").split('\n')
	Problem(inp, sys.argv[1])
