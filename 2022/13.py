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

	def get_package(self, str, i:list[int]):
		content = []
		while i[0] < len(str):
			if str[i[0]] == ']':
				i[0] += 1
				return content
			if str[i[0]] == '[':
				i[0] += 1
				content.append(self.get_package(str, i))
				continue
			elif str[i[0]] != ',':
				number = ""
				while (str[i[0]] != ',' and str[i[0]] != ']'):
					number += str[i[0]]
					i[0] += 1
				content.append(int(number))
			else:
				i[0] += 1	
		return -1

	def compare(self, first, second):
		"""Return 1 if less than, 0 if equal, -1 if greater than"""
		# print("Comparing")
		# print(first)
		# print("and")
		# print(second)
		if isinstance(first, int) and isinstance(second, int):
			if first < second:
				return 1
			elif first == second:
				return 0
			else:
				return -1
		if (type(first) != type(second)):
			if isinstance(first, int):
				first = [first]
			else:
				second = [second]
			return self.compare(first, second)
		i = 0
		while i < len(first) and i < len(second):
			comparision = self.compare(first[i], second[i])
			if comparision != 0:
				return comparision
			i += 1
		if len(first) < len(second):
			return 1
		elif len(first) == len(second):
			return 0
		else:
			return -1

	def part1(self):
		indexes = []
		for i in range(len(self.inp)):
			first_str, second_str = self.inp[i].split()
			index = [1]
			first = self.get_package(first_str, index)
			index = [1]
			second = self.get_package(second_str, index)
			if self.compare(first, second) == 1:
				indexes.append(i+1)
		print(indexes)
		return sum(indexes)

	def part2(self):
		packages = []
		for i in range(len(self.inp)):
			first_str, second_str = self.inp[i].split()
			index = [1]
			first = self.get_package(first_str, index)
			index = [1]
			second = self.get_package(second_str, index)
			packages.append(first)
			packages.append(second)
		divider1 = [[2]]
		divider2 = [[6]]
		packages.append(divider1)
		packages.append(divider2)
		for i in range(len(packages)-1):
			for j in range(i+1, len(packages)):
				if self.compare(packages[i], packages[j]) == -1:
					packages[i], packages[j] = packages[j], packages[i]
		index1 = packages.index(divider1) + 1
		index2 = packages.index(divider2) + 1
		print(index1, index2)
		return index1 * index2

if __name__ == "__main__":
	inp = read_file("Inputs/input13.txt").split('\n\n')
	Problem(inp, sys.argv[1])
