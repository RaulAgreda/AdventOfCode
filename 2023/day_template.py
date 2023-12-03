import sys
import os

DAY = sys.argv[1]

template = f"""import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp:str, part:str):
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
	if (len(sys.argv) != 2):
		print("Usage: python3 {DAY}.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input{DAY}.txt").split('\\n')
	Problem(inp, sys.argv[1])
"""
if not os.path.exists(f"{DAY}.py"):
	with open(f"{DAY}.py", "w") as f:
		f.write(template)
else:
	print("Python file already exists")

if not os.path.exists(f"Inputs/input{DAY}.txt"):
	with open(f"Inputs/input{DAY}.txt", "w") as f:
		f.write("")
else:
	print("Input file already exists")
