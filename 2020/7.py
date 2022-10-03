import ReadInput
rules = ReadInput.convert("7_Input","\n")

holderBags = []

# Part 1
def getRuleBag(rule):
    return rule.split(" bags ")[0]

# def contains(bags,rule):
#     for bag in bags:
#         if bag in rule:
#             return True
#     return False

# for rule in rules:
#     if "shiny gold" in rule:
#         holderBags.append(getRuleBag(rule))
# for i in range(5):
#     for rule in rules:
#         if contains(holderBags,rule):
#             newBag = getRuleBag(rule)
#             if newBag not in holderBags:
#                 holderBags.append(newBag)

# print(holderBags)
# print(len(holderBags))

# Part 2
bagTypes = [rule.split(" bags ")[0] for rule in rules]

def getRule(bag):
    return rules[bagTypes.index(bag)]

def countBags(bag):
    rule = getRule(bag)
    
    if "no other bags" in rule:
        return 0
    
    count = []
    bags = []
    otherBags = rule.split()[4:]

    for i in range(len(otherBags)):
        if i % 4 == 0:
            count.append(int(otherBags[i]))
        elif i % 4 == 1:
            bags.append(otherBags[i] + " " + otherBags[i + 1])

    mult = 0
    for i in range(len(count)):
        mult += count[i] * countBags(bags[i]) + count[i]
    return mult



print(countBags("shiny gold"))