import ReadInput
adapters = ReadInput.convertToInt("10_Input")

# Part 1
# difference1 = 1
# difference3 = 1

# adapters.sort()
# for i in range(len(adapters)-1):
#     if adapters[i+1] - adapters[i] == 1:
#         difference1 += 1
#     elif adapters[i+1] - adapters[i] == 3:
#         difference3 += 1

# print(difference1, difference3,difference1 + difference3 - len(adapters))

# Part 2
adapters.sort()
adapters.insert(0,0)
memo = {adapters[-1]: 1}

def compatibleAdapters(adapt: int,adapters: list):
    start = adapters.index(adapt)
    compatible = []
    for i in range(start + 1, start + 4):
        if i >= len(adapters):
            break
        if adapters[i] <= adapters[start] + 3:
            compatible.append(adapters[i])

    return compatible

def numWays(adapt,memo):

    if adapt not in memo:
        compatible = compatibleAdapters(adapt,adapters)
        memo[adapt] = 0
        for nextAdapt in compatible:
            memo[adapt] += numWays(nextAdapt,memo)
            
        return memo[adapt]
    else:
        return memo[adapt]

print(numWays(adapters[0],memo))
        
print("Al fin D:")

