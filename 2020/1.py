import ReadInput

entry = ReadInput.convertToInt("1_Input")

result = 0

# Part 1
# for i in range(len(entry) - 1):
#     for j in range(i,len(entry)):
#         if entry[i] + entry[j]  == 2020:
#             result = entry[i] * entry[j]

# Part 2
for i in range(len(entry) - 1):
    for j in range(i,len(entry)):
        for k in range(j, len(entry)):
            if entry[i] + entry[j] + entry[k] == 2020:
                result = entry[i] * entry[j] * entry[k]

print(result)