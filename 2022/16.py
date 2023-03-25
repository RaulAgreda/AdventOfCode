import sys
from Inputs.ReadFile import *

graph = {
    'AA': {'flow': 'value', 'tunnels': ['valve2', 'valve3']},
}

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		self.memoize = {}
		self.graph = self.parseInput()
		print(self.graph)
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())
	
	def parseInput(self):
		graph = {}
		for line in self.inp:
			valve_data = line.split(' ')
			valve = valve_data[1]
			rate = int(valve_data[4].split('=')[1][:-1])
			tunnels = [v.strip(',') for v in valve_data[9:]]
			graph[valve] = {'rate': rate, 'tunnels': tunnels}
		return graph

	def get_max_pressure(self, valve, remaining_time):
		if remaining_time <= 0:
			return 0
		if remaining_time in self.memoize[valve]:
			return self.memoize[valve][remaining_time]
		# We have two cases, either we release the pressure or we don't
		# If we don't release the pressure
		max_pressure = 0
		for next_valve in self.graph[valve]['tunnels']:
			max_pressure = max(max_pressure, self.get_max_pressure(next_valve, remaining_time - 1))
		# If we release the pressure
		preassure_released = self.graph[valve]['rate'] * (remaining_time - 1)
		for next_valve in self.graph[valve]['tunnels']:
			max_pressure = max(max_pressure, preassure_released + self.get_max_pressure(next_valve, remaining_time - 2))
		# Store the result
		self.memoize[valve][remaining_time] = max_pressure
		return max_pressure
		

	def part1(self):
		self.memoize = {}
		for valve in self.graph:
			self.memoize[valve] = {}
		result = self.get_max_pressure('AA', 30)
		for mem in self.memoize:
			print(mem, self.memoize[mem])
		return result

	def part2(self):
		pass

if __name__ == "__main__":
	inp = read_file("Inputs/input16.txt").split('\n')
	Problem(inp, sys.argv[1])
