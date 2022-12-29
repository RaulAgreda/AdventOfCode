import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		""" Represented by x, y offset coordinates in the folowing form
			(0, 1) (1, 1)
			(0, 0) (1, 0)

			####

			.#.
			###
			.#.

			..#
			..#
			###

			#
			#
			#
			#

			##
			##
		"""
		self.shapes = (
			((0,0),(1,0),(2,0),(3,0)),
			((1,0),(0,1),(1,1),(2,1),(1,2)),
			((0,0),(1,0),(2,0),(2,1),(2,2)),
			((0,0),(0,1),(0,2),(0,3)),
			((0,0),(1,0),(0,1),(1,1)),
		)
		self.WIDE = 7
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def rock_move(self, pos, shape, filled, direction):
		"""True if move is posible, False if cancels"""
		for offset in shape:
			x = pos[0] + offset[0] + direction
			y = pos[1] + offset[1]
			if x < 0 or x >= self.WIDE or (x, y) in filled:
				return False
		return True

	def rock_fall(self, pos, shape, filled):
		"""Returns if the rock stopped moving or not"""
		collides = False
		for offset in shape:
			x = pos[0] + offset[0]
			y = pos[1] + offset[1] - 1
			if y < 0 or (x, y) in filled:
				collides = True
				break
		if collides:
			for offset in shape:
				x = pos[0] + offset[0]
				y = pos[1] + offset[1]
				if y > self.tallest_point:
					self.tallest_point = y
				filled.add((x, y))
		return collides
			
	def print_filled(self, filled, shape, block_pos):
		for y in range(self.tallest_point + 4, -1, -1):
			for x in range(self.WIDE):
				printed_shape = False
				for offset in shape:
					if x == block_pos[0] + offset[0] and y == block_pos[1] + offset[1]:
						print('O', end='')
						printed_shape = True
						break
				if not printed_shape:
					if (x, y) in filled:
						print('#', end='')
					else:
						print('.', end='')
			print()
		print("\n")
	

	def part1(self):
		self.tallest_point = -1
		current_shape = 0
		filled = set()
		movement_idx = 0
		for i in range(2022):
			pos = [2, self.tallest_point + 4]
			current_shape = i % len(self.shapes)
			while True:
				direction = 1 if self.inp[movement_idx] == '>' else -1
				movement_idx = (movement_idx + 1) % len(self.inp)
				if self.rock_move(pos, self.shapes[current_shape], filled, direction):
					pos[0] += direction
				if not self.rock_fall(pos, self.shapes[current_shape], filled):
					pos[1] -= 1
				else:
					break
		return self.tallest_point + 1

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input17.txt")
	Problem(inp, sys.argv[1])
