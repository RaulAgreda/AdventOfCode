import ReadInput
dataInputs = ReadInput.convert("4_Input","\n\n")

count = 0

validDataInputs = []


# Part 1 q sirva pal 2 :v
for inp in dataInputs:
    inpSplit = inp.split()
    contains_cid = False
    for key in inpSplit:
        if "cid" in key:
            contains_cid = True
            break
    if len(inpSplit) == 8 or (len(inpSplit) == 7 and not contains_cid):
        validDataInputs.append(inpSplit)

def checkValid(data):
    # print(data)
    key = data[0:3]
    value = data[4:]

    if key == "byr":
        if 1920 <= int(value) <= 2002:
            return True
    elif key == "iyr":
        if 2010 <= int(value) <= 2020:
            return True
    elif key == "eyr":
        if 2020 <= int(value) <= 2030:
            return True
    elif key == "hgt":
        if "cm" in value:
            if 150 <= int(value[:-2]) <= 193:
                return True
        elif "in" in value:
            if 59 <= int(value[:-2]) <= 76:
                return True
    elif key == "hcl":
        validCharac = "0123456789abcdef"

        hcl_valid = True
        for c in validCharac:
            if c not in validCharac:
                valid =  False
                break
        if value[0] == "#" and hcl_valid:
            return True        
    elif key == "ecl":
        validDat = ("amb","blu","brn","gry","grn","hzl","oth")
        for ecl in validDat:
            if value == ecl:
                return True
        
    elif key == "pid":
        if len(value) == 9:
            return True
    elif key == "cid":
        return True

    return False

for validData in validDataInputs:
    valid = True
    for data in validData:
        if not checkValid(data):
            valid = False
            break
    if valid:
        count+=1

print(count)
