from utils.terminal_colors import Colors
from utils.read_input import read_input, read_test
from problem.problem import Problem
import importlib
import sys, os
from typing import *



class Main:
    def __init__(self, argv):
        self.check_arguments(argv)

        self.day = argv[1].zfill(2)
        self.part = argv[2]
        if "-t" in argv:
            self.run_tests()
            sys.exit(0)
        
        input = read_input(f"days/{self.day}/input.txt")

        print(f"{Colors.YELLOW}Solution: {Colors.RESET}{self.solve_problem(input, self.part)}")

    def solve_problem(self, input: str, part: str):
        # Dynamically import the module for the specified day
        day_module = importlib.import_module(f"days.{self.day}.{self.day}")

        # Get the Problem class from the imported module
        Problem = getattr(day_module, f"Day{self.day}")
        
        return Problem(input, part).get_solution()

    def check_arguments(self, argv):
        if len(argv) not in (3, 4):
            print("Usage: python3 main.py DAY PART [-t]")
            print("\tDAY: 1, 2, ..., 25")
            print("\tPART: 1 or 2")
            print("\t-t: run tests")
            sys.exit(1)


    def run_tests(self):
        # Read every test file of the TestInputs/Part_{part} folder
        test_files = os.listdir(f"days/{self.day}/TestInputs/Part_{self.part}")
        for test_file in test_files:
            with open(f"days/{self.day}/TestInputs/Part_{self.part}/{test_file}", "r") as f:
                content = f.read()
                input_text, expected_solution = content.split("SOLUTION:\n")
                input_text = input_text.replace("INPUT:\n", "")[:-1]
                expected_solution = expected_solution.replace("\n", "")
                expected_solution = expected_solution.replace("\r", "")
                expected_solution = expected_solution.strip()
                result = str(self.solve_problem(input_text, self.part))
                self.do_unit_test(result, expected_solution, test_file.split(".")[0])


    def do_unit_test(self, result:str, expected_solution:str, name: str):
        if result == expected_solution:
            print(f"{Colors.GREEN}[OK] {Colors.RESET}Test {name} passed!!")
        else:
            print(f"{Colors.RED}[ERROR] {Colors.RESET}Test {name} failed!!")
            print(f"{Colors.YELLOW}\tExpected: {Colors.RESET}{expected_solution}")
            print(f"{Colors.YELLOW}\tGot: {Colors.RESET}{result}")

if __name__ == "__main__":
    Main(sys.argv)