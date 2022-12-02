import ReadInput

class Solution:        
    def getNumbers(self,numbStr,split = " "):
        nums = numbStr.split(split)
        while "" in nums:
            nums.remove("")

        for i in range(len(nums)):
            nums[i] = int(nums[i])
        return nums
    
    def getBoards(self,boardList):

        boards = [[]]
        i = 0
        for line in boardList:
            
            if line != "":
                boards[i].append(self.getNumbers(line))
            else:
                boards.append([])
                i+=1

        return boards

    def checkWinner(self,marksDic,boards,winnersList):
        for b in range(len(boards)):
            if b not in winnersList:
                row = {0:0,1:0,2:0,3:0,4:0}
                column = {0:0,1:0,2:0,3:0,4:0}
                for key in marksDic[b].keys():
                    row[key[0]] += 1
                    column[key[1]] += 1
                    
                for k in row.keys():
                    if row[k] == 5:
                        return b
                for k in column.keys():
                    if column[k] == 5:
                        return b

        return None

    def part1(self):    
        inp = ReadInput.convert("4_Input.txt")
        nums = self.getNumbers(inp[0],",")
        boards = self.getBoards(tuple(inp[2:]))

        marks = {}
        for b in range(len(boards)):
            marks[b] = {}

        winner = None
        finalNumber = -1
        # Mark numbers
        for n in nums:
            if winner == None:
                for b in range(len(boards)):
                    found = False
                    board = boards[b]
                    # marks[b] = {}
                    for i in range(len(board)):
                        for j in range(len(board)):
                            if board[i][j] == n:
                                found = True
                                marks[b][(i,j)] = n
                                break
                        if found:
                            break
            else:
                break
            # print(marks)
            winner = self.checkWinner(marks,boards,[])
            finalNumber = n

        unMarkSum = 0

        for i in range(len(boards[winner])):
            for j in range(len(boards[winner][i])):
                if (i,j) not in marks[winner].keys():
                    unMarkSum += boards[winner][i][j]

        return unMarkSum*finalNumber    

    def part2(self):

        inp = ReadInput.convert("4_Input.txt")
        nums = self.getNumbers(inp[0],",")
        boards = self.getBoards(tuple(inp[2:]))

        marks = {}

        boards = boards.copy()
        for b in range(len(boards)):
            marks[b] = {}

        winner = None
        finalNumber = -1
        winners = []
        # Mark numbers
        for n in nums:
            for b in range(len(boards)):
                if b not in winners:
                    found = False
                    board = boards[b]
                    # marks[b] = {}
                    for i in range(len(board)):
                        for j in range(len(board)):
                            if board[i][j] == n:
                                found = True
                                marks[b][(i,j)] = n
                                break
                        if found:
                            break

            # print(marks)
            if found:
                winner = self.checkWinner(marks,boards,winners)
                while winner is not None:
                    winners.append(winner)
                    # print(len(boards)) 
                    finalNumber = n
                    # print("last winner", winner,"with",n)
                    winner = self.checkWinner(marks,boards,winners)

        winner = winners[-1]
        unMarkSum = 0

        for i in range(len(boards[winner])):
            for j in range(len(boards[winner][i])):
                if (i,j) not in marks[winner].keys():
                    unMarkSum += boards[winner][i][j]

        return unMarkSum*finalNumber    

sol = Solution()
print(sol.part1())