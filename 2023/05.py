import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp:str, part:str):
		# Format is [seeds, firstMap, secondMap, ...]
		self.inp = inp
		self.seeds = [int(x) for x in inp[0].split()[1:]]
		# Each maps initialy contains the header wich we don't want
		self.maps_arrays = []
		for map in self.inp[1:]:
			values = map.split('\n')[1:]
			for i in range(len(values)):
				values[i] = [int(x) for x in values[i].split()]
			self.maps_arrays.append(values)
		
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

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
	if (len(sys.argv) != 2):
		print("Usage: python3 05.py [1|2]")
		sys.exit(1)
	inp = read_file("Inputs/input05.txt").split('\n\n')
	Problem(inp, sys.argv[1])
