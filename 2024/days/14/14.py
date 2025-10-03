from typing import *
from template.problem import Problem
import time

# WIDTH = 11
# HEIGHT = 7
WIDTH = 101
HEIGHT = 103

class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{(self.x, self.y)}"

class Robot:
    def __init__(self, p: V2, v: V2):
        self.p = p
        self.v = v

    def move(self, t: int):
        self.p.x = (self.p.x + self.v.x * t) % WIDTH
        self.p.y = (self.p.y + self.v.y * t) % HEIGHT
        return self.p

class Day14(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def getRobot(self, line: str):
        p,v = line.split()
        px, py = p.split(',')
        vx, vy = v.split(',')
        return Robot(V2(int(px[2:]), int(py)), V2(int(vx[2:]), int(vy)))

    def part1(self):
        robots = {}
        q1 = q2 = q3 = q4 = 0
        for line in self.input:
            robot = self.getRobot(line)
            robot.move(100)

            if robot.p.x < WIDTH // 2 and robot.p.y < HEIGHT // 2:
                q1 += 1
            elif robot.p.x > WIDTH // 2 and robot.p.y < HEIGHT // 2:
                q2 += 1
            elif robot.p.x > WIDTH // 2 and robot.p.y > HEIGHT // 2:
                q3 += 1
            elif robot.p.x < WIDTH // 2 and robot.p.y > HEIGHT // 2:
                q4 += 1
            key = (robot.p.x, robot.p.y)
            if key not in robots:
                robots[key] = 1
            else:
                robots[key] += 1
        self.printGrid(robots)

        print(q1, q2, q3, q4)
        return q1 * q2 * q3 * q4

    def printGrid(self, robots):
        for y in range(HEIGHT):
            text = ""
            for x in range(WIDTH):
                if (x,y) in robots:
                    text+=str(robots[(x,y)])
                else:
                    text+='.'
            print(text)

    def part2(self):
        robots = []
        for line in self.input:
            robots.append(self.getRobot(line))
        it = 0
        while it < WIDTH * HEIGHT:
            it += 1
            robotsDict = {}
            for robot in robots:
                robot.move(1)
                key = (robot.p.x, robot.p.y)
                if key not in robotsDict:
                    robotsDict[key] = 1
                else:
                    robotsDict[key] += 1
            # Basically I ran the simulation until I found a strange horizontal pattern, since there
            # iteration 79, because each +HEIGHT iterations the y would be the same for each robot,
            # eventually the robots would assemble only moving horizontally
            # Automating this is not easy as you don't know how the drawing would be, at first
            # I thought that every robot would form the tree, and I was trying to find a symmetry
            # but, neither the tree is centered nor all robots assemble to the tree
            if (79 - it) % HEIGHT == 0:
                print("It:", it)
                self.printGrid(robotsDict)
                time.sleep(0.25)            
        return
