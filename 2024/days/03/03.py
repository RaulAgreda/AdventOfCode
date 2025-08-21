from typing import *
from template.problem import Problem

class Day03(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def part1(self):
        result = 0
        self.input = '\n'.join(self.input)
        a = ""
        b = ""
        c = 0
        r = 0
        while c < len(self.input):
            char = self.input[c]
            # print(char)
            if r == 0 and char == 'm' and self.input[c:c+4] == "mul(":
                c+=3
                r+=1
            elif r == 1 and char.isdigit():
                while self.input[c].isdigit():
                    a+=self.input[c]
                    c+=1
                c-=1
                r+=1
            elif r == 2 and char == ',':
                r+=1
            elif r == 3 and char.isdigit():
                while self.input[c].isdigit():
                    b+=self.input[c]
                    c+=1
                c-=1
                r+=1
            elif r == 4 and char == ')':

                result += int(a) * int(b)
                a = ""
                b = ""
                r = 0
            else:
                a = ""
                b = ""
                r = 0
            c+=1
        return result

    def part2(self):
        enabled = True
        result = 0
        self.input = '\n'.join(self.input)
        a = ""
        b = ""
        c = 0
        r = 0
        while c < len(self.input):
            char = self.input[c]
            # print(char)
            if r == 0 and char == 'm' and self.input[c:c+4] == "mul(":
                c+=3
                r+=1
            elif r == 1 and char.isdigit():
                while self.input[c].isdigit():
                    a+=self.input[c]
                    c+=1
                c-=1
                r+=1
            elif r == 2 and char == ',':
                r+=1
            elif r == 3 and char.isdigit():
                while self.input[c].isdigit():
                    b+=self.input[c]
                    c+=1
                c-=1
                r+=1
            elif r == 4 and char == ')':
                if enabled:
                    result += int(a) * int(b)
                a = ""
                b = ""
                r = 0
            else:
                a = ""
                b = ""
                r = 0
            if char == "d":
                if self.input[c:c+4] == "do()":
                    enabled = True
                elif self.input[c:c+7] == "don't()":
                    enabled = False
            c+=1

        # Add your solution for part 1 here
        return result
