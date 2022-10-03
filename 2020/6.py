import ReadInput
groups = ReadInput.convert("6_Input","\n\n")

# Part 1
# vocals = "abcdefghijklmnopqrstuvwxyz"

# counts = []

# for group in groups:
#     group = group.replace("\n","")
#     counts.append(0)
#     for v in vocals:
#         if v in group:
#             counts[-1]+=1

# Part 2
count = 0
for group in groups:
    persons = group.split("\n")
    answers = []
    for person in persons:
        for c in person:
            if c not in answers:
                answers.append(c)
    n_answers = 0
    for answer in answers:
        answerRepeated = True
        for person in persons:
            if answer not in person:
                answerRepeated = False
        if answerRepeated:
            n_answers += 1
    count += n_answers

print(count)


# print(sum(counts))