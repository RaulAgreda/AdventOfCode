import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		# Format is [seeds, firstMap, secondMap, ...]
		if not test:
			inp = read_file("Inputs/input05.txt")
		else:
			inp, solutions = read_test("TestInputs/input05.txt")
			
		self.inp = inp.split("\n\n")
		
		self.seeds = [int(x) for x in self.inp[0].split()[1:]]
		# Each maps initialy contains the header wich we don't want
		self.maps_arrays = []
		for map in self.inp[1:]:
			values = map.split('\n')[1:]
			for i in range(len(values)):
				values[i] = [int(x) for x in values[i].split()]
			self.maps_arrays.append(values)
		
		result = self.part1() if part == '1' else self.part2()
		if not test:
			print(result)
		else:
			solution = solutions[0] if part == '1' else solutions[1]
			self.do_unit_test(str(result), solution)

	def do_unit_test(self, result:str, solution:str):
		if str(result) == solution:
			print(f"{Colors.GREEN}[OK] {Colors.RESET}The example result is correct!!")
		else:
			print(f"{Colors.RED}[ERROR] {Colors.RESET}The example result is wrong!!")
			print(f"{Colors.YELLOW}Expected: {Colors.RESET}{solution}")
			print(f"{Colors.YELLOW}Got: {Colors.RESET}{result}")

	def part1(self):
		minim = None
		for seed in self.seeds:
			nextVal = seed
			for conversionPack in self.maps_arrays:
				for conversion in conversionPack:
					dest, source, step = conversion
					# nextVal e [source, source + step]
					if source <= nextVal and nextVal < source + step:
						diff = nextVal - source
						nextVal = dest + diff
						break
			if minim is None or nextVal < minim:
				minim = nextVal
		return minim

	def part2(self):
		locations = {}
		print("starting")
		# To optimize it, if we get a greater number in some of the steps, skip it by breaking the current range loop
		# Skip all numbers that doesn't reach the minimum value
		minim = None
		for s in range(0, len(self.seeds), 2):
			start = self.seeds[s]
			end = start + self.seeds[s+1]
			i = 0
			while start < start+1:
				seed = start
				start += 1
				if minim and start > minim:
					break
				nextVal = seed
				for conversionPack in self.maps_arrays:
					for conversion in conversionPack:
						dest, source, step = conversion
						# nextVal e [source, source + step]
						if source <= nextVal and nextVal < source + step:
							diff = nextVal - source
							nextVal = dest + diff
							break
				if minim is None or nextVal < minim:
					minim = nextVal
				# print(nextVal)
		return minim

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 05.py 1|2 [-t]")
		print("1: run part1\n2: run part2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
