import sys
from Inputs.ReadFile import *

class Problem:
	def __init__(self, inp, part):
		self.inp = inp
		self.sensors = {}
		self.beacons = set()
		self.get_data()
		self.manhatan_dists = {sensor: self.manhatan_dist(sensor, self.sensors[sensor]) for sensor in self.sensors}
		print(self.manhatan_dist)
		if part == '1':
			print(self.part1())
		else:
			print(self.part2())


	def get_data(self):
		for line in self.inp:
			sensor, beacon = line.split(': ')
			sensor_x_part, sensor_y_part = sensor.split(', ')
			sensor_x = int(sensor_x_part.split('=')[1])
			sensor_y = int(sensor_y_part.split('=')[1])
			beacon_x_part, beacon_y_part = beacon.split(', ')
			beacon_x = int(beacon_x_part.split('=')[1])
			beacon_y = int(beacon_y_part.split('=')[1])
			self.sensors[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
			self.beacons.add((beacon_x, beacon_y))


	def manhatan_dist(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	def part1(self):
		illegal_positions = set()
		Y = 2000000
		for sensor in self.sensors:
			manhatan_dist = self.manhatan_dist(sensor, self.sensors[sensor])
			x_distance = manhatan_dist - abs(Y - sensor[1])
			if x_distance >= 0:
				x = -x_distance
				while x <= x_distance:
					new_pos = (sensor[0] + x, Y)
					if new_pos not in self.sensors and new_pos not in self.beacons:
						illegal_positions.add(new_pos)
					x += 1
		return len(illegal_positions)

	def part2(self):
		Limit = 20
		x = 0
		while x <= Limit:
			y = 0
			while y <= Limit:
				a = True
				for sensor in self.manhatan_dists:
					if self.manhatan_dists[sensor] >= self.manhatan_dist((x, y), sensor):
						a = False
						break
				if a:
					return x * 4000000 + y
				y += 1
			x += 1
						



if __name__ == "__main__":
	inp = read_file("Inputs/input15.txt").split('\n')
	Problem(inp, sys.argv[1])
