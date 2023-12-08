import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors
from typing import *

class Node:
	def __init__(self, name:str):
		self.name = name
		self.left: Node = None
		self.right: Node = None

	def pushNodes(self, left:'Node', right:'Node'):
		self.left = left
		self.right = right

class Problem:
	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input08.txt")
		else:
			inp, solutions = read_test("TestInputs/input08.txt")

		self.sequence, self.inp = inp.split("\n\n")

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
	
	def parseLine(self, line):
		line = line.split(" = ")
		parent = line[0]
		locations = line[1].split(", ")
		left = locations[0][1:]
		right = locations[1][:-1]
		return parent, left, right

	def getNetwork(self)-> Dict[str, Node]:
		nodes = {}
		network = self.inp.split('\n')
		for n in network:
			parent, left, right = self.parseLine(n)
			nodes[parent] = Node(parent)
			parent: Node = nodes[parent]
			if left in nodes:
				left = nodes[left]
			else:
				left = Node(left)
			if right in nodes:
				right = nodes[right]
			else:
				right = Node(right)
			parent.pushNodes(left, right)
		return nodes

	def part1(self):
		nodes = self.getNetwork()
		c_node = 'AAA'
		i = 0
		while c_node != 'ZZZ':
			dir = self.sequence[i % len(self.sequence)]
			if dir == 'L':
				c_node = nodes[c_node].left.name
			else:
				c_node = nodes[c_node].right.name
			i += 1
		return i

	def calculate_lcm(self, x, y):
		# Find the greatest common divisor (GCD) using the Euclidean algorithm
		def calculate_gcd(a, b):
			while b:
				a, b = b, a % b
			return a
		
		# Calculate the LCM using the relationship: LCM(a, b) = (a * b) / GCD(a, b)
		gcd = calculate_gcd(x, y)
		lcm = (x * y) // gcd
    
		return lcm
	
	def part2(self):
		nodes = self.getNetwork()
		startNodes = []
		knownLengths:Dict[str, int] = {}
		for n in nodes:
			if n[-1] == 'A':
				startNodes.append(n)
		currentNodes = startNodes.copy()
		i = 0
		while len(knownLengths) != len(startNodes):
			dir = self.sequence[i % len(self.sequence)]
			for n in range(len(currentNodes)):
				if startNodes[n] in knownLengths:
					continue
				if dir == 'L':
					currentNodes[n] = nodes[currentNodes[n]].left.name
				else:
					currentNodes[n] = nodes[currentNodes[n]].right.name

				if currentNodes[n][-1] == 'Z':
					knownLengths[startNodes[n]] = i + 1
			i+=1
		lcm = 1
		for l in knownLengths:
			lcm = self.calculate_lcm(lcm, knownLengths[l])
		return lcm

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 08.py 1|2 [-t]")
		print("1: run part1\n2: run part2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	