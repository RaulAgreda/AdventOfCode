import sys
from Inputs.ReadFile import *

class Package:
	def __init__(self):
		self.deep = 0
		self.content = []
	
	def append(self, item):
		self.content.append(item)

	def __getitem__(self, key):
		return self.content[key]

	def __str__(self):
		return str(self.content)

	def __lt__(self, other):
		print(self, other)
		while self.deep != other.deep:
			conversion = Package()
			if self.deep < other.deep:
				conversion.append(self)
				conversion.deep = self.deep + 1
				self = conversion
			else:
				conversion.append(other)
				conversion.deep = other.deep + 1
				other = conversion
			print(conversion)
		return self.content < other.content
				

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())

	def get_package(self, str, i:list[int], current_deep, deep:list[int]):
		content = []
		current_deep += 1
		while i[0] < len(str):
			if str[i[0]] == ']':
				i[0] += 1
				if deep[0] < current_deep:
					deep[0] = current_deep
				return content
			if str[i[0]] == '[':
				i[0] += 1
				content.append(self.get_package(str, i, current_deep, deep))
				continue
			elif str[i[0]] != ',':
				content.append(int(str[i[0]]))
			i[0] += 1	
		return -1

	def part1(self):
		indexes = []
		for i in range(len(self.inp)):
			first_str, second_str = self.inp[i].split()
			index = [1]
			deep = [0]
			first = self.get_package(first_str, index, 0, deep)
			first_deep = deep[0]
			print(first)
			print("first", first_deep)
			index = [1]
			deep = [0]
			second = self.get_package(second_str, index, 0, deep)
			second_deep = deep[0]
			print(second)
			print("second", second_deep)
			while first_deep != second_deep:
				conversion = []
				if first_deep < second_deep:
					conversion.append(first)
					first_deep += 1
					first = conversion
				else:
					conversion.append(second)
					second_deep += 1
					second = conversion
			if first < second:
				print(i)
				indexes.append(i)
		return indexes

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input13.txt").split('\n\n')
	Problem(inp, sys.argv[1])
