import ReadInput

inpts = ReadInput.convert("18_Input.txt")

def extractInterParenthesis(expr):
    """Returns the last index where ')' closes"""
    stack = []
    do = True
    # stack.append("(")
    last = None
    start = 1
    i = 0
    while len(stack) > 0 and i < len(expr) or do:
        if expr[i] == "(":
            do = False
            # print("Hey")
            stack.append("(")
            if last is None:
                start = i
        elif expr[i] == ")":
            if last is None:
                last = i
            stack.remove("(")
        i+=1
        
    return expr[start+1:last], start, last

def operate(exp):
    exp = exp.split(" ")
    # print(exp)
    while "+" in exp:
        index = exp.index("+")
        o1 = int(exp[index - 1])
        o2 = int(exp[index + 1])
        exp[index-1] = o1 + o2
        exp.pop(index)
        exp.pop(index)

    while "*" in exp:
        index = exp.index("*")
        o1 = int(exp[index - 1])
        o2 = int(exp[index + 1])
        exp[index-1] = o1 * o2
        exp.pop(index)
        exp.pop(index)

    return exp[0]

inp = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

total = 0

for inp in inpts:
    while type(inp) is not int:
        if "(" in inp:

            parenth = extractInterParenthesis(inp)
            start = parenth[1]

            result = operate(parenth[0])

            inp = inp[:start] + str(result) + inp[parenth[2]+1:]

        else:
            inp = operate(inp)
    total+=inp

print(total)