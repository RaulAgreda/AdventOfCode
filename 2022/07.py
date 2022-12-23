import sys
from Inputs.ReadFile import *
import re

class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size

class Dir:
	def __init__(self, name, parent):
		self.parent = parent
		self.name = name
		self.size = 0
		# self.files = []
		self.dirs = {}

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def build_directories(self):
		root_dir = Dir("/", None)
		current_dir = root_dir
		for line in self.inp:
			params = line.split()
			if params[0] == "$":
				if params[1] == "cd":
					if params[2] == "..":
						current_dir = current_dir.parent
					elif params[2] != "/":
						current_dir = current_dir.dirs[params[2]]
				else:
					continue
			elif params[0] == "dir":
				current_dir.dirs[params[1]] = Dir(params[1], current_dir)
			else:
				current_dir.size += int(params[0])
		return root_dir

	def set_sizes(self, root_dir):
		self.set_dir_size(root_dir)

	def set_dir_size(self, dir):
		if (len(dir.dirs) == 0):
			return dir.size
		for d in dir.dirs:
			dir.size += self.set_dir_size(dir.dirs[d])
		return dir.size

	def get_sum_dirs_size_with_value_below(self, dir, n, total):
		if dir.size < n:
			total[0] += dir.size
		for d in dir.dirs:
			self.get_sum_dirs_size_with_value_below(dir.dirs[d], n, total)
		return total[0]

	def part1(self):
		root_dir = self.build_directories()
		self.set_sizes(root_dir)
		total = [0]
		self.get_sum_dirs_size_with_value_below(root_dir, 100000, total)
		return total[0]

	def check_min_size(self, dir, min_space, min_selected_space):
		if dir.size >= min_space:
			min_selected_space[0] = min(min_selected_space[0], dir.size)
		for d in dir.dirs:
			self.check_min_size(dir.dirs[d], min_space, min_selected_space)


	def part2(self):
		root_dir = self.build_directories()
		self.set_sizes(root_dir)
		available_space = 70000000 - root_dir.size
		min_space = 30000000 - available_space
		min_selected_space = [root_dir.size]
		self.check_min_size(root_dir, min_space, min_selected_space)
		return min_selected_space[0]



if __name__ == "__main__":
	inp = read_file("Inputs/input07.txt").split('\n')
	if inp[-1] == "":
		inp.pop()
	Problem(inp, sys.argv[1])
