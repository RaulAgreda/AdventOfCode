import sys
import os
from utils.terminal_colors import Colors
from dotenv import load_dotenv
import requests

load_dotenv()
input_cookie = os.getenv("AOC_COOKIE")

def create_file(inputFile, content):
	if not os.path.exists(inputFile):
		os.makedirs(os.path.dirname(inputFile), exist_ok=True)
		with open(inputFile, "w") as f:
			f.write(content)
	else:
		print(Colors.RED+"[ERROR]"+Colors.RESET, inputFile, "already exists!!")
		exit(1)

def download_problem():
	# Download and generate url file
	url = f"https://adventofcode.com/2024/day/{int(DAY)}"
	try:
		problem = requests.get(url)
		problem.raise_for_status()
		create_file(f"days/{DAY}/problem.url", url)

	except requests.exceptions.RequestException as e:
		print(Colors.RED+"[ERROR]"+Colors.RESET, "Failed to download problem:", e)
		exit(1)


def download_input():
	try:
		inp = requests.get(f"https://adventofcode.com/2024/day/{int(DAY)}/input", cookies={"session": input_cookie})
		inp.raise_for_status()
		create_file(f"days/{DAY}/input.txt", inp.text[:-1])
	except requests.exceptions.RequestException as e:
		print(Colors.RED+"[ERROR]"+Colors.RESET, "Failed to download input:", e)
		exit(1)

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("Usage: python3 day_template.py [DAY]")
		sys.exit(1)
	DAY = sys.argv[1].zfill(2)

	with open("problem/template.txt", "r") as f:
		template = f.read()
		template = template.replace("[day]", DAY)

	create_file(f"days/{DAY}/{DAY}.py", template)
	download_problem()
	download_input()
	create_file(f"days/{DAY}/TestInputs/Part_1/1.txt", "INPUT:\n<input_text>\nSOLUTION:\n<solution_part1>")
	create_file(f"days/{DAY}/TestInputs/Part_2/1.txt", "INPUT:\n<input_text>\nSOLUTION:\n<solution_part2>")
