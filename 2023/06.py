import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp:str, part:str):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def parseInput(self, ignoreSpaces:bool):
		times = self.__getNums(self.inp[0], ignoreSpaces)
		distances = self.__getNums(self.inp[1], ignoreSpaces)
		return times, distances

	def __getNums(self, string:str, ignoreSpaces:bool):
		list = []
		currentNum = ''
		for c in string:
			if c.isdigit():
				currentNum += c
			elif not ignoreSpaces:
				if currentNum != '':
					list.append(currentNum)
					currentNum = ''
		list.append(currentNum)
		currentNum = [int(x) for x in list]
		return currentNum
	

	def part1(self):
		# x = t (T-t)
		times, distances = self.parseInput(ignoreSpaces=False)
		result = 1
		for i in range(len(times)):
			ways = 0
			T = times[i]
			D = distances[i]
			t = 1
			while t < T:
				x = t * (T - t)
				if x > D:
					ways += 1
				t+=1
			if ways > 0:
				result *= ways
		return result
	
	def part2(self):
		times, distances = self.parseInput(ignoreSpaces=True)
		T = times[0]
		D = distances[0]
		t = 1
		min_t = 1
		max_t = T
		while t < T:
			x = t * (T - t)
			if x > D:
				min_t = t
				break
			t+=1
		t = T
		while t > 0:
			x = t * (T - t)
			if x > D:
				max_t = t
				break
			t -= 1
		return max_t - min_t + 1
		

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 06.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input06.txt").split('\n')
	Problem(inp, sys.argv[1])
	