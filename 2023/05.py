import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

class Range:
	def __init__(self, start:int , length:int = None, stop:int = None):
		self.start:int = start
		if stop is None:
			self.length:int = length
			self.stop:int = start + length - 1
		else:
			self.length = stop - start + 1
			self.stop = stop
		if self.length == 0:
			print("[ERROR] RANGE SHOULD NOT HAVE LENGTH 0")

	def __contains__(self, n: int):
		return self.start <= n <= self.stop

	def __str__(self):
		return f"[{self.start}, {self.stop}]"

class RangeMap:
	def __init__(self, dest:int|None, src:int|None, step:int):
		self.dest=Range(dest, step) if dest is not None else None
		self.src=Range(src, step) if src is not None else None
		self.step = step
		
	def __gt__(self, other: 'RangeMap'):
		return self.dest.start > other.dest.start

	def fitRange(self, r:Range) -> Range:
		"""Searchs in this map, if it is not included at all, returns r\n
			if it is partially included:
			- if r.start is in range, returns [r.start + src, length] were length is the number of numbers included in dest
			- else, returns [r.start, r.dest]
		"""
		if r.start > self.dest.stop or r.stop < self.dest.start:
			return r
		if r.start in self.dest:
			if r.stop <= self.dest.stop:
				return r
			else:
				return Range(r.start, stop=self.dest.stop)
		else:
			return Range(r.start, stop=self.dest.start - 1)
		
	def convertRange(self, r:Range) -> Range:
		"""[other] => [self.dest] => [self.src]"""
		if r.start in self.dest:
			diff = r.start - self.dest.start
			return Range(self.src.start + diff, r.length)
		else:
			return r
		
		

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

	def inSeeds(self, r: Range, seeds:List[Range]):
		for sR in seeds:
			# If the ranges collide, return the lowest value
			if r.start <= sR.stop and r.stop >= sR.start:
				if r.start <= sR.start:
					return sR.start
				else:
					return r.start
		return None
	
	def getLowest(self, checkRange:Range, c:int, allMaps:List[RangeMap], seeds):
		if c == len(allMaps):
			lowest = self.inSeeds(checkRange, seeds)
			if lowest is None:
				return None, checkRange.length
			else:
				offset = lowest - checkRange.start
				return offset, checkRange.length

		for m in allMaps[c]:
			print("=======Checking======")
			print(m.dest, m.src, m.step)
			nextCheck = checkRange
			while True:
				fit = m.fitRange(nextCheck)
				print(nextCheck,"fit in", fit)
				conversion = m.convertRange(fit)
				print("\t converted in:", conversion)
				result = self.getLowest(conversion, c+1, allMaps, seeds)
				if result[0] is not None:
					return fit.start - checkRange.start + result[0], result[1]
				if fit.stop == checkRange.stop:
					break
				nextCheck = Range(fit.stop + 1, stop=checkRange.stop)
		return None, None


	def part2(self):
		seeds = []
		for s in range(0, len(self.seeds), 2):
			seeds.append(Range(self.seeds[s], self.seeds[s+1]))
		for conversionPack in self.maps_arrays:
			for c in range(len(conversionPack)):
				conversionPack[c] = RangeMap(*conversionPack[c])
			conversionPack.sort()
		self.maps_arrays.reverse()
		for ms in self.maps_arrays:
			for m in ms:
				print(m.dest, m.src)
			print("=======")
		# for m in self.maps_arrays[-1]:
		# 	print(m.dest.start, m.src.start, m.step)
		startRange = Range(0, stop=self.maps_arrays[0][-1].dest.stop)
		return self.getLowest(startRange, 0, self.maps_arrays, seeds)
		print(startRange)

		return None

	def test_ranges(self):
		test1 = Range(3, 7) # [2, 8]
		splitTest = []
		splitTest.append(RangeMap(0, 0, 11)) # [0, 10]
		splitTest.append(RangeMap(1, 0, 3)) # [0, 10]
		splitTest.append(RangeMap(0, 0, 7))# [0, 6]
		splitTest.append(RangeMap(4, 0, 7))# [4, 10]
		splitTest.append(RangeMap(4, 0, 3))# [4, 6]
		splitTest.append(RangeMap(10, 0, 12))
		splitTest.append(RangeMap(1, 0, 2))
		def testCase(inputRange: Range, splitTest:RangeMap):
			print(f"Fit {inputRange} in {splitTest.dest}")
			result = splitTest.fitRange(test1)
			print(result)
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
