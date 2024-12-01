import sys
import os
from utils.terminal_colors import Colors

def create_file(inputFile, content):
	if not os.path.exists(inputFile):
		with open(inputFile, "w") as f:
			f.write(content)
	else:
		print(Colors.RED+"[ERROR]"+Colors.RESET, inputFile, "already exists!!")

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("Usage: python3 day_template.py [DAY]")
		print("Recommended format: python3 day_template.py 01")
		sys.exit(1)
	DAY = sys.argv[1]

	template = f"""import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input{DAY}.txt")
		else:
			inp, solutions = read_test("TestInputs/input{DAY}.txt")

		self.inp = inp.split("\\n")
		
		result = self.part1() if part == '1' else self.part2()
		if not test:
			print(result)
		else:
			solution = solutions[0] if part == '1' else solutions[1]
			self.do_unit_test(str(result), solution)

	def do_unit_test(self, result:str, solution:str):
		if result == solution:
			print(f"{{Colors.GREEN}}[OK] {{Colors.RESET}}The example result is correct!!")
		else:
			print(f"{{Colors.RED}}[ERROR] {{Colors.RESET}}The example result is wrong!!")
			print(f"{{Colors.YELLOW}}Expected: {{Colors.RESET}}{{solution}}")
			print(f"{{Colors.YELLOW}}Got: {{Colors.RESET}}{{result}}")
	
	def part1(self):
		pass

	def part2(self):
		pass

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 {DAY}.py 1|2 [-t]")
		print("1: run part 1\\n2: run part 2\\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	"""

	create_file(f"{DAY}.py", template)
	create_file(f"Inputs/input{DAY}.txt", "")
	create_file(f"TestInputs/input{DAY}.txt", "INPUT:\n<input_text>\nSOLUTION:\n<solution_part1>\n<solution_part2>")
