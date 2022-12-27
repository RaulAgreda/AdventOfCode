import sys
from Inputs.ReadFile import *
import os
import time

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def load_map_blocks(self):
		blocks = set()
		for path in self.inp:
			segments = path.split(' -> ')
			for seg in range(len(segments)-1):
				start_x, start_y = [int(x) for x in segments[seg].split(',')]
				end_x, end_y = [int(x) for x in segments[seg + 1].split(',')]
				x = start_x
				while x <= end_x:
					blocks.add((x,start_y))
					x+=1
				x = start_x
				while x >= end_x:
					blocks.add((x,start_y))
					x-=1
				y = start_y
				while y <= end_y:
					blocks.add((start_x,y))
					y+=1
				y = start_y
				while y >= end_y:
					blocks.add((start_x,y))
					y-=1
		return blocks

	def get_limits(self, blocks):
		"""Returns the limits of the map in the form of (min_x, min_y, max_x, max_y)"""
		min_x = 500
		min_y = 0
		max_x = 0
		max_y = 0
		for block in blocks:
			x, y = block
			if x < min_x:
				min_x = x
			if x > max_x:
				max_x = x
			if y > max_y:
				max_y = y
		min_x -= 1
		max_x += 1
		max_y += 1
		return min_x, min_y, max_x, max_y

	def fill_sand(self, blocks):
		Limit = self.limits[3]
		sand = set()
		while True:	
			new_sand = [500,0]
			stop = blocks | sand
			while new_sand[1] < Limit:
				new_sand[1] += 1
				if (new_sand[0], new_sand[1]) in stop:
					new_sand[0] -= 1
					if (new_sand[0], new_sand[1]) in stop:
						new_sand[0] += 2
						if (new_sand[0], new_sand[1]) in stop:
							new_sand[0] -= 1
							new_sand[1] -= 1
							sand.add((new_sand[0], new_sand[1]))
							# if len(sand) % 3 == 0:
							# 	#Just printing for fun
							# 	self.print_map(blocks, sand)
							# 	print()
							# 	time.sleep(0.1)
							break
			if new_sand[1] >= Limit:
				break
		return sand

	def fill_sand_part2(self, blocks):
		Limit = self.limits[3]
		sand = set()
		i = 0
		while True:	
			new_sand = [500,0]
			stop = blocks | sand
			while new_sand[1] < Limit:
				new_sand[1] += 1
				if (new_sand[0], new_sand[1]) in stop:
					new_sand[0] -= 1
					if (new_sand[0], new_sand[1]) in stop:
						new_sand[0] += 2
						if (new_sand[0], new_sand[1]) in stop:
							new_sand[0] -= 1
							new_sand[1] -= 1
							sand.add(tuple(new_sand))
							if tuple(new_sand) == (500,0):
								return sand
							i+=1
							if len(sand) % 1000 == 0:
								print(len(sand))
							break

	def part1(self):
		blocks = self.load_map_blocks()
		self.limits = self.get_limits(blocks)
		sand = self.fill_sand(blocks)
		self.print_map(blocks, sand)
		return len(sand)

	def part2(self):
		blocks = self.load_map_blocks()
		self.limits = self.get_limits(blocks)
		self.inp.append(f'-9999,{self.limits[3] + 1} -> 9999,{self.limits[3] + 1}')
		blocks = self.load_map_blocks()
		self.limits = self.get_limits(blocks)
		sand = self.fill_sand_part2(blocks)
		self.print_map(blocks, sand)
		return len(sand)

	def print_map(self, blocks, sand):
		min_x, min_y, max_x, max_y = self.limits
		for y in range(min_y, max_y+1):
			for x in range(min_x, max_x+1):
				if (x, y) == (500, 0):
					print('+', end=' ')
				elif (x, y) in blocks:
					print('#', end=' ')
				elif (x, y) in sand:
					print('O', end=' ')
				else:
					print('.', end=' ')
			print()

if __name__ == "__main__":
	inp = read_file("Inputs/input14.txt").split('\n')
	Problem(inp, sys.argv[1])
