from typing import *
from template.problem import Problem
import math

class Stone:
    """Nodo individual de la lista enlazada"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getDigits(self):
        if self.val == 0:
            return 1
        return int(math.log10(self.val)) + 1
    
    def __str__(self):
        return str(self.val)

class LinkedList:
    """Implementación de una lista enlazada simple"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """Añade un elemento al final de la lista"""
        new_node = Stone(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def insertAfter(self, node: Stone, newNodeVal):
        newNode = Stone(newNodeVal, node.next)
        node.next = newNode
        self.size += 1
    
    def is_empty(self):
        """Verifica si la lista está vacía"""
        return self.head is None
    
    def __len__(self):
        """Retorna el tamaño de la lista"""
        return self.size
    
    def __str__(self):
        """Representación en string de la lista"""
        if not self.head:
            return "[]"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.val))
            current = current.next
        
        return "" + " ".join(elements) + ""


class Day11(Problem):
    def __init__(self, input: str, part: str):
        # Call the parent class constructor to initialize input and part
        super().__init__(input, part)
    
    def getDigits(self, val):
        if val == 0:
            return 1
        return int(math.log10(val)) + 1

    def blink(self, val, it, maxIt):
        if it == maxIt - 1:
            return 1
        if val == 0:
            return self.blink(1, it+1, maxIt)
        n = self.getDigits(val)
        if n % 2 == 0:
            fact = 10 ** (n//2)
            a, b = val // fact, val % fact
            return self.blink(a, it+1, maxIt) + self.blink(b, it+1, maxIt)
        return self.blink(val*2024, it +1, maxIt)
            
        

    def part1(self, iterations = 25):
        startStones = [int(x) for x in self.input[0].split()]
        stones = LinkedList()
        for stone in startStones:
            stones.append(stone)
        # Apply rules:
        it = 0
        while it < iterations:
            print(it)
            stone = stones.head
            while stone is not None:
                if stone.val == 0:
                    stone.val = 1
                    stone = stone.next
                    continue
                n = stone.getDigits()
                if n % 2 == 0:
                    fact = 10 ** (n//2)
                    a, b = stone.val // fact, stone.val % fact
                    stone.val = a
                    stones.insertAfter(stone, b)
                    stone = stone.next.next
                else:
                    stone.val *= 2024
                    stone = stone.next
            it+=1
        return len(stones)

    def part2(self):
        return self.part1(75)
