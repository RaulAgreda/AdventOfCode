import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

class Range:
	def __init__(self, start:int , length: int):
		self.start:int = start
		self.length:int = length
		self.stop:int = start + length - 1
		if self.length == 0:
			print("[ERROR] RANGE SHOULD NOT HAVE LENGTH 0")

	def __str__(self):
		return f"[{self.start}, {self.stop}]"

class RangeMap:
	def __init__(self, dest:int|None, src:int|None, step:int):
		self.dest=Range(dest, step) if dest is not None else None
		self.src=Range(src, step) if src is not None else None
		self.step = step
		
	def __gt__(self, other: 'RangeMap'):
		return self.dest.start < other.src.start

	def splitInRanges(self, inputRange:Range) -> List[Range]:
		"""Compares the input range with the dest range, and splits the input range in order to fit the dest"""
		dest = self.dest
		if inputRange.stop < dest.start or dest.stop < inputRange.start:
			return None
		if inputRange.start >= dest.start and inputRange.stop <= dest.stop:
			return [inputRange]
		ranges:List[Range] = []
		if inputRange.start < dest.start:
			ranges.append(Range(inputRange.start, dest.start - inputRange.start))
			ranges.append(Range(dest.start, inputRange.length - ranges[-1].length))
		if inputRange.stop > dest.stop:
			if len(ranges) == 0:
				ranges.append(Range(inputRange.start, dest.stop - inputRange.start + 1))
			else:
				ranges[-1] = Range(ranges[-1].start, dest.stop - ranges[-1].start + 1)
			ranges.append(Range(dest.stop+1, inputRange.stop - dest.stop))
		return ranges


	def convertRange(self, other:Range) -> Range:
		"""[other] => [self.dest] => [self.src]"""
		diff = other.start - self.dest.start
		return Range(self.src.start + diff, other.length)
		
		

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

	def checkRange(self, range: Range, maps: List[RangeMap], startOffset: int):
		for m in maps:
			spl = m.splitInRanges(range)
			if spl is None:
				continue
			for s in spl:
				offset = s.start - range.start
				conversion = m.convertRange(s)
				self.checkRange(conversion, maps, offset)


	def part2(self):
		seeds = []
		for s in range(0, len(self.seeds), 2):
			seeds.append(Range(self.seeds[s], self.seeds[s+1]))
		for seed in seeds:
			print(seed)
		for conversionPack in self.maps_arrays:
			for c in range(len(conversionPack)):
				conversionPack[c] = RangeMap(*conversionPack[c])
			conversionPack.sort()
		print("============")
		for m in self.maps_arrays[-1]:
			print(m.dest, m.src, m.step)

		return None

	def test_ranges():
		test1 = Range(2, 7) # [2, 8]
		splitTest = []
		splitTest.append(RangeMap(0, 0, 11)) # [0, 10]
		splitTest.append(RangeMap(0, 0, 7))# [0, 6]
		splitTest.append(RangeMap(4, 0, 7))# [4, 10]
		splitTest.append(RangeMap(4, 0, 3))# [4, 6]
		splitTest.append(RangeMap(10, 0, 12))
		splitTest.append(RangeMap(1, 0, 2))
		def testCase(inputRange: Range, splitTest:RangeMap):
			print(f"Fit {inputRange} in {splitTest.dest}")
			result = splitTest.splitInRanges(inputRange)
			for r in result:
				print(r)
			print("=====")
		for test in splitTest:
			testCase(test1, test)
if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 05.py 1|2 [-t]")
		print("1: run part1\n2: run part2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
