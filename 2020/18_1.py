import ReadInput

inpts = ReadInput.convert("18_Input.txt")

results = []

def extractParenthesis(expr,backwards):
    """Returns the last index where ')' closes"""
    stack = []
    if not backwards:
        stack.append("(")

        i = 1
        while len(stack) > 0:
            if expr[i] == "(":
                stack.append("(")
            elif expr[i] == ")":
                stack.remove("(")
            i+=1

        return expr[1:i-1]
    else:
        stack.append(")")

        i = len(expr) - 2

        while len(stack) > 0:
            if expr[i] == ")":
                stack.append(")")
            elif expr[i] == "(":
                stack.remove(")")
            i-=1
        
        return expr[i+2:-1],i

def operate(expr):
    if len(expr) == 1:
        return int(expr)
    else:
        i = len(expr) - 1

        if expr[i] == ")":
            extracted = extractParenthesis(expr,True)
            if extracted[1] <= 0:
                return operate(expr[1:-1])
            o2 = extracted[0]
            op = expr[extracted[1]-1]
            o1 = expr[:extracted[1]-2]

        else:
            o2 = expr[i]
            op = expr[i-2]
            o1 = expr[:i-3]
        

        return operate(o1) + operate(o2) if op == "+" else operate(o1) * operate(o2)


# inp = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
total = 0

for inp in inpts:
    total += operate(inp)

print(total)