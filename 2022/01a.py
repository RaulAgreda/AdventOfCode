from Inputs.ReadFile import *

inp = read_file("Inputs/input01.txt").split("\n\n")
elfs_total = []

for elf in inp:
	numbers = []
	for x in elf.split("\n"):
		if x != "":
			numbers.append(int(x))
	elfs_total.append(sum(numbers))

print(max(elfs_total))
