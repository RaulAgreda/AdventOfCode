import sys
from Inputs.ReadFile import *
import queue

class Node:
	def __init__(self, value, i , j):
		self.id = (i, j)
		self.value = value
		self.posib = []

	# operator overloading for <, >, <=, >=, ==, !=
	def __lt__(self, other):
		return ord(self.value) < ord(other.value)
	def __gt__(self, other):
		return ord(self.value) > ord(other.value)
	def __le__(self, other):
		return ord(self.value) <= ord(other.value)
	def __ge__(self, other):
		return ord(self.value) >= ord(other.value)
	def __eq__(self, other):
		return ord(self.value) == ord(other.value)
	def __ne__(self, other):
		return ord(self.value) != ord(other.value)

class Problem:
	def __init__(self, inp, part):
		self.inp = inp

		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def create_nodes(self):
		Start = None
		End = None
		M = self.inp
		nodes = []
		for i in range(len(M)):
			nodes.append([])
			for j in range(len(M[0])):
				if M[i][j] == 'S':
					new_node = Node(M[i][j], i, j)
					Start = new_node
				elif M[i][j] == 'E':
					new_node = Node(M[i][j], i, j)
					End = new_node
				else:
					new_node = Node(M[i][j], i, j)
				nodes[i].append(new_node)	
		for i in range(len(M)):
			for j in range(len(M[0])):
				if i > 0:
					if self.can_go(nodes[i][j].value, nodes[i-1][j].value):
						nodes[i][j].posib.append(nodes[i-1][j])
				if i < len(M) - 1:
					if self.can_go(nodes[i][j].value, nodes[i+1][j].value):
						nodes[i][j].posib.append(nodes[i+1][j])
				if j > 0:
					if self.can_go(nodes[i][j].value, nodes[i][j-1].value):
						nodes[i][j].posib.append(nodes[i][j-1])
				if j < len(M[0]) - 1:
					if self.can_go(nodes[i][j].value, nodes[i][j+1].value):
						nodes[i][j].posib.append(nodes[i][j+1])
		return Start, End
		
	def dijkstra(self, Start, End):
		q = queue.PriorityQueue()
		q.put((0, Start))
		visited = set()
		while not q.empty():
			current = q.get()
			if current[1] == End:
				return current[0]
			if current[1].id not in visited:
				visited.add(current[1].id)
				for node in current[1].posib:
					if node.id not in visited:
						q.put((current[0] + 1, node))
		return -1

	def can_go(self, current, next):
		return abs(ord(current) - ord(next)) <= 1

	def part1(self):
		Start, End = self.create_nodes()
		return self.dijkstra(Start, End)

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input12.txt").split('\n')
	Problem(inp, sys.argv[1])
