from typing import *
from template.problem import Problem
import math

class Day13(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        # super().__init__(input, part)
        games = input.split('\n\n')
        self.games = []
        for game in games:
            self.games.append(self.getGameValues(game))
        self.solution = self.part1() if part == '1' else self.part2()
    
    def getGameValues(self, game):
        lines = game.split('\n')
        la = lines[0].split()
        lb = lines[1].split()
        lp = lines[2].split()
        Xa = int(la[2][2:-1])
        Ya = int(la[3][2:])
        Xb = int(lb[2][2:-1])
        Yb = int(lb[3][2:])
        Xp = int(lp[1][2:-1])
        Yp = int(lp[2][2:])
        return Xa, Ya, Xb, Yb, Xp, Yp

    def part1(self):
        # Yep I used maths
        total = 0
        for game in self.games:
            p = self.get_cost(*game)
            if p:
                total += p
        return total

    def part2(self):
        total = 0
        for game in self.games:
            Xa, Ya, Xb, Yb, Xp, Yp = game
            Xp += 10000000000000
            Yp += 10000000000000
            p = self.get_cost(Xa, Ya, Xb, Yb, Xp, Yp)
            if p:
                total += p
        return total

    def get_cost(self, Xa, Ya, Xb, Yb, Xp, Yp):
        det = Xa * Yb - Ya * Xb
        if det == 0:
            return None

        numA = Xp * Yb - Yp * Xb
        numB = Xa * Yp - Ya * Xp

        # Si no dividen exactamente, no hay solución entera
        if numA % det != 0 or numB % det != 0:
            return None

        A = numA // det
        B = numB // det
        # A y B deberían ser >= 0
        if A < 0 or B < 0:
            return None

        cost = A * 3 + B
        return cost
