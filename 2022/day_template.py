import sys

DAY = sys.argv[1]

template = f"""import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def part1(self):
		pass

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input{DAY}.txt").split('\\n')
	Problem(inp, sys.argv[1])
"""

with open(f"{DAY}.py", "w") as f:
	f.write(template)

with open(f"Inputs/input{DAY}.txt", "w") as f:
	f.write("")