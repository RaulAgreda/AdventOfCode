import ReadInput

def part1():
    rulesInp = ReadInput.convert("19_Input.txt")

    rules = {}
    wordsIndx = rulesInp.index("") + 1
    for rule in rulesInp:
        if rule == "":
            break
        
        colonIdx = rule.index(":")
        i = rule[:colonIdx]
        rules[i] = rule[colonIdx + 2:]
        if '"' in rules[str(i)]:
            rules[i] = rules[i][1]

    messages = []

    for i in range(wordsIndx,len(rulesInp)):
        messages.append(rulesInp[i])


    def getCombinations(set1,set2):
        comb = set()
        for word1 in set1:
            for word2 in set2:
                comb.add(word1+word2)
        return comb

    
    sentences = {}

    def getWords(rule,rules,sentences):

        if rule not in sentences.keys():
            if len(rules[rule]) == 1:
                sentences[rule] = set(rules[rule][0])
                return sentences[rule]
            else:
                combinations = []
                
                parts = rules[rule].split(" | ")
                for part in parts:
                    uncomComb = []
                    rul = part.split(" ")
                    for c in rul:
                        uncomComb.append(getWords(c,rules,sentences))

                    for i in range(len(uncomComb) - 1):
                        uncomComb[i+1] = getCombinations(uncomComb[i],uncomComb[i+1])

                    combinations.append(uncomComb[-1])
                if len(combinations) > 1:
                    for word in combinations[1]:
                        combinations[0].add(word) 
                sentences[rule] = combinations[0]
                return sentences[rule]
        else:
            return sentences[rule]
            
    getWords("0",rules,sentences)

    # for rule in sentences.keys():
    #     print(sentences[rule])

    total = 0

    for msg in messages:
        if msg in sentences["0"]:
            total+=1

    return total

print(part1())
