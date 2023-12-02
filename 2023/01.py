import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp:str, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def part1(self):
		values = []
		first = None
		last = None
		for line in self.inp:
			i = 0
			while i < len(line):
				if line[i].isdigit():
					first = line[i]
					break
				i+=1
			i = len(line) - 1
			while i >= 0:
				if line[i].isdigit():
					last = line[i]
					break
				i-=1
			values.append(int(first + last))
		return sum(values)

	def part2(self):
		validDigits = {
			"one": '1',
			"two": '2',
			"three": '3',
			"four": '4',
			"five": '5',
			"six": '6',
			"seven": '7',
			"eight": '8',
			"nine": '9'
		}
		values = []
		first = None
		last = None
		for line in self.inp:
			first = None
			c = 0
			while c < len(line):
				val = None
				if line[c].isdigit():
					val = line[c]
					if val is not None and first is None:
						first = val
				for j in range(3, 6):
					subs = line[c:c+j]
					if subs in validDigits:
						val = validDigits[subs]
					if val is not None and first is None:
						first = val
				if val is not None:
					last = val
				c+=1
			values.append(int(first + last))
		return sum(values)

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage: python3 01.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input01.txt").split('\n')
	Problem(inp, sys.argv[1])
