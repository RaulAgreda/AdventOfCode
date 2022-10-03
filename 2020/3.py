import ReadInput

treeMap = ReadInput.convert("3_Input")

# Part 1
# position = [0,0]
# nTrees = 0
# while position[1] + 1 < len(treeMap):
#     position[0] += 3
#     position[1] += 1
#     if position[0] >= len(treeMap[0]):
#         position[0] = position[0]-len(treeMap[0])
#     # print(position)
#     # print(len(treeMap[0]),len(treeMap))
#     if treeMap[position[1]][position[0]] == "#":
#         nTrees+=1
# print(nTrees)

# Part 2
def findTrees(slope):
    position = [0,0]
    nTrees = 0
    while position[1] + slope[1] < len(treeMap):
        position[0] = (position[0] + slope[0])%len(treeMap[0])
        position[1] += slope[1]

        if treeMap[position[1]][position[0]] == "#":
            nTrees+=1
    return nTrees

slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))
result = 1
for slope in slopes:
    result *= findTrees(slope)

print(result)

