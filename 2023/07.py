import sys
from utils.read_input import read_file, read_test
from utils.terminal_colors import Colors

class Hand:
	class Types:
		HIGH_CARD = 0,
		ONE_PAIR = 1,
		TWO_PAIR = 2,
		THREE_OF_A_KIND = 3,
		FULL_HOUSE = 4,
		FOUR_OF_A_KIND = 5,
		FIVE_OF_A_KIND = 6,
	
	CARD_STRENGHT = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

	def __init__(self, cards:str, withJokers=False) -> None:
		self.cards = cards
		self.jokers = withJokers
		if withJokers:
			self.type = self.__getTypeWithJokers()
		else:
			self.type = self.__getType()

	def compareCard(self, card1, card2) -> int:
		"""< 0: card1 less than card2
		= 0: card1 equal to card2
		> 0: card1 greater than card2
		"""
		card1_val = Hand.CARD_STRENGHT[card1]
		card2_val = Hand.CARD_STRENGHT[card2]
		if self.jokers:
			if card1 == 'J':
				card1_val = 13
			if card2 == 'J':
				card2_val = 13
		return card2_val - card1_val


	def __gt__(self, other) -> bool:
		if self.type != other.type:
			return self.type > other.type
		for i in range(len(self.cards)):
			result = self.compareCard(self.cards[i], other.cards[i])
			if result != 0:
				return result > 0
		print("I shouldn't be executing xD")
		

	def __lt__(self, other) -> bool:
		return not self.__gt__(other)


	def __getType(self):
		cards = {}
		for card in self.cards:
			cards[card] = 0
		for card in self.cards:
			cards[card] += 1

		if len(cards) == 1:
			return Hand.Types.FIVE_OF_A_KIND
		elif len(cards) == 2:
			first_value = list(cards.values())[0]
			if first_value in (1, 4):
				return Hand.Types.FOUR_OF_A_KIND
			else:
				return Hand.Types.FULL_HOUSE
		elif len(cards) == 3:
			for card in cards:
				if cards[card] == 3:
					return Hand.Types.THREE_OF_A_KIND
			return Hand.Types.TWO_PAIR
		elif len(cards) == 4:
			return Hand.Types.ONE_PAIR
		else:
			return Hand.Types.HIGH_CARD
		
	def __getTypeWithJokers():
		return "a"

class Problem:

	'''
	@param part: 1 or 2
	@param test: True if we are checking the example
	'''
	def __init__(self, part:str, test:bool):
		if not test:
			inp = read_file("Inputs/input07.txt")
		else:
			inp, solutions = read_test("TestInputs/input07.txt")

		self.inp = inp.split("\n")
		result = self.part1() if part == '1' else self.part2()
		if not test:
			print(result)
		else:
			solution = solutions[0] if part == '1' else solutions[1]
			self.do_unit_test(str(result), solution)

	def do_unit_test(self, result:str, solution:str):
		if result == solution:
			print(f"{Colors.GREEN}[OK] {Colors.RESET}The example result is correct!!")
		else:
			print(f"{Colors.RED}[ERROR] {Colors.RESET}The example result is wrong!!")
			print(f"{Colors.YELLOW}Expected: {Colors.RESET}{solution}")
			print(f"{Colors.YELLOW}Got: {Colors.RESET}{result}")
	
	def parseInput(self):
		hands = []
		bids = []
		for line in self.inp:
			hand, bid = line.split()
			hand = Hand(hand)
			bid = int(bid)
			hands.append(hand)
			bids.append(bid)
		return hands, bids


	def part1(self):
		hands, bids = self.parseInput()
		for i in range(len(hands)-1):
			for j in range(i+1, len(hands)):
				if hands[i] > hands[j]:
					hands[i], hands[j] = hands[j], hands[i]
					bids[i], bids[j] = bids[j], bids[i]
		total = 0
		for i in range(len(hands)):
			total += bids[i] * (i+1)
		return total

	def part2(self):
		pass

if __name__ == "__main__":
	if (len(sys.argv) not in (2, 3)):
		print("Usage: python3 07.py 1|2 [-t]")
		print("1: run part1\n2: run part2\n[-t]: run test example")
		sys.exit(1)
	doTest = "-t" in sys.argv
	Problem(sys.argv[1], doTest)
	