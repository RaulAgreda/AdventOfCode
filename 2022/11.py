import sys
from Inputs.ReadFile import *
import queue

class Monkey():
	def __init__(self, starting_items, operation, op2, divisible, if_true, if_false):
		self.items = starting_items
		self.add_operation = True if operation == 'add' else False
		self.op2 = op2
		self.divisible = divisible
		self.if_true = if_true
		self.if_false = if_false
		self.inspected = 0
	
	def inspect_item(self):
		item = self.items.pop(0)
		self.inspected += 1
		if self.add_operation:
			item = self.add(item, self.op2)
		else:
			item = self.multiply(item, self.op2)
		item //= 3
		next_monkey = self.test(item)
		return next_monkey, item

	def inspect_items(self, monkeys, mod):
		while(not self.items.empty()):
			item = self.items.get()
			self.inspected += 1
			if self.add_operation:
				item = self.add(item, self.op2)
			else:
				item = self.multiply(item, self.op2)
			if item % self.divisible == 0:
				next_monkey = self.if_true
			else:
				next_monkey = self.if_false
			item %= mod
			monkeys[next_monkey].items.put(item)
	
	def add_item(self, item):
		self.items.append(item)
		

	def test(self, item):
		return self.if_true if item % self.divisible == 0 else self.if_false

	def add(self, x, y = None):
		if y is None:
			return x + x
		return x + y

	def multiply(self, x, y = None):
		if y is None:
			return x * x
		return x * y

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		self.monkeys = self.get_monkeys()
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def get_monkeys(self):
		monkeys = []
		for monk_definition in self.inp:
			lines = monk_definition.split('\n')
			items_list = [int(x) for x in lines[1].split(':')[1].split(", ")]
			starting_items = queue.Queue(10000)
			for item in items_list:
				starting_items.put(item)
			operation = lines[2].split('= ')[1]
			operator = None
			if '*' in lines[2]:
				op2 = lines[2].split('* ')[1]
				operation = 'multiply'
				if op2 != 'old':
					operator = int(op2)
			else:
				op2 = lines[2].split('+ ')[1]
				operation = 'add'
				if op2 != 'old':
					operator = int(op2)

			condition = int(lines[3].split('by ')[1])
			if_true = int(lines[4].split('monkey ')[1])
			if_false = int(lines[5].split('monkey ')[1])
			monkeys.append(Monkey(starting_items, operation, operator, condition, if_true, if_false))
		return monkeys

	def part1(self):
		for i in range(20):
			for monkey in self.monkeys:
				while len(monkey.items) > 0:
					next_monkey, item = monkey.inspect_item()
					self.monkeys[next_monkey].add_item(item)
		inspections = []
		for monkey in self.monkeys:
			inspections.append(monkey.inspected)
		inspections.sort()
		return inspections[-1] * inspections[-2]
				

	def part2(self):
		i = 0
		mod = 1
		for monkey in self.monkeys:
			mod *= monkey.divisible
		while i < 10000:
			i += 1
			for monkey in self.monkeys:
				monkey.inspect_items(self.monkeys, mod)
		inspections = []
		for monkey in self.monkeys:
			inspections.append(monkey.inspected)
		inspections.sort()
		return inspections[-1] * inspections[-2]

if __name__ == "__main__":
	inp = read_file("Inputs/input11.txt").split('\n\n')
	Problem(inp, sys.argv[1])
