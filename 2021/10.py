
import ReadInput

def part1():
    lines = ReadInput.convert("10_Input.txt")

    def getPoints(syntanx):
        stack = []
        open = {"(":0,"[":1,"{":2,"<":3}
        close = {")":0,"]":1,"}":2,">":3}
        points = {0:3,1:57,2:1197,3:25137}
        for c in syntanx:
            if c in open:
                stack.append(c)
            elif c in close:
                if close[c] == open[stack[-1]]:
                    stack.pop()
                else:
                    return points[close[c]]
        return 0

    total = 0

    for line in lines:
        total += getPoints(line)

    return total


def part2():

    lines = ReadInput.convert("10_Input.txt")

    def getPoints(syntanx):
        stack = []
        open = {"(":0,"[":1,"{":2,"<":3}
        close = {")":0,"]":1,"}":2,">":3}
        points = {0:3,1:57,2:1197,3:25137}
        for c in syntanx:
            if c in open:
                stack.append(c)
            elif c in close:
                if close[c] == open[stack[-1]]:
                    stack.pop()
                else:
                    return points[close[c]]
        return 0
    
    def getCompletionPoints(syntanx):
        stack = []
        open = {"(":0,"[":1,"{":2,"<":3}
        close = {")":0,"]":1,"}":2,">":3}
        points = {0:1,1:2,2:3,3:4}
        for c in syntanx:
            if c in open:
                stack.append(c)
            elif c in close:
                stack.pop()

        # print(stack)

        total = 0

        for c in stack[::-1]:
            total = total * 5 + points[open[c]]
                
        return total

    valids = []

    # print(getCompletionPoints("<{([{{}}[<[[[<>{}]]]>[]]"))

    for line in lines:
        if getPoints(line) == 0:
            valids.append(line)

    points = []

    for valid in valids:
        points.append(getCompletionPoints(valid))

    points.sort()
    # print(points)
    return points[len(points)//2]
    


print(part2())


