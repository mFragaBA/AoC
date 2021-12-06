def markBoards(boards, number):
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[0][i][j] == number:
                    board[1][i][j] = True

def fullRow(board, row):
    return all(board[1][row][j] == True for j in range(5))

def fullCol(board, col):
    return all(board[1][j][col] == True for j in range(5))

def winner(board):
    return any(fullRow(board, i) or fullCol(board, i) for i in range(5))

def computeScore(board, num):
    return sum(int(board[0][i][j]) if board[1][i][j] == False else 0 for i in range(5) for j in range(5)) * int(num)

with open('input.txt') as infile:
    contents = [l.strip(' \n') for l in infile.readlines()]

numbers = contents[0].split(',')

boards = []
i = 0
boardsStr = contents[2:]
while(i < len(boardsStr)):
    board = []
    for j in range(5):
       board.append([x for x in boardsStr[i+j].split(' ') if x != '']) 
    boards.append((board, [[False for _ in range(5)] for _ in range(5)]))

    i+= 6

#print(boards)

for number in numbers:
    markBoards(boards, number)
    for board in boards:
        if winner(board):
            score = computeScore(board, number)
            print(score)
            exit()

