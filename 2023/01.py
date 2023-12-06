import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input01.txt")
		else:
			inp, solutions = read_test("TestInputs/input01.txt")

		self.inp = inp.split("\n")
		
		result = self.part1() if part == '1' else self.part2()
		if not test:
			print(result)
		else:
			solution = solutions[0] if part == '1' else solutions[1]
			self.do_unit_test(str(result), solution)

	def do_unit_test(self, result:str, solution:str):
		if result == solution:
			print(f"{Colors.GREEN}[OK] {Colors.RESET}The example result is correct!!")
		else:
			print(f"{Colors.RED}[ERROR] {Colors.RESET}The example result is wrong!!")
			print(f"{Colors.YELLOW}Expected: {Colors.RESET}{solution}")
			print(f"{Colors.YELLOW}Got: {Colors.RESET}{result}")
	
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
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 01.py 1|2 [-t]")
		print("1: run part1\n2: run part2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	