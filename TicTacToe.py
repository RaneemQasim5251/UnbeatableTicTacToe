# initialize empty board position then print it
def printBoard(board):
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('-  +  -  +  -')
    print(board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('-  +  -  +  -')
    print(board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print("\n")

# method checks if the space is free or not
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):        # first check the availability of position
        board[position] = letter
        printBoard(board)            # notify the user that he has good changes and that was free position
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!") # which is never going to happen ha ha
                exit()

        return


    else:
        print("Can't insert there!")                           # if the space isn't free
        position = int(input("Please enter new position:  "))  # ask again for position,
                                                               # convert it to int cause we wanna input int value
        insertLetter(letter, position)
        return


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# turns which playes has won
def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False           # if there are still available spaces return false
    return True                    # if there are none available spaces we return true and it's a draw

# method to takes the input and insert tries to insert the letters
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


def compMove():
    bestScore = -800 # start with a low score
    bestMove = 0  # random move (initialize)
    for key in board.keys(): # go over each possible move
        if (board[key] == ' '): # if the position is empty
            board[key] = bot
            score = minimax(board, 0, False)  # minmax function
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing): # isMaximizing boolean value, we actually don't need depth in tic-tac-toe
                                         # beacause it is simple, but I put it in to not forget it if I need it...
                                         # ...in more complicated scenarios.

    if (checkWhichMarkWon(bot)):       # check bot
        return 1
    elif (checkWhichMarkWon(player)):  # check player
        return -1
    elif (checkDraw()):
        return 0

# our AI bot let say (qam)
    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

# qam enemy bot
    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()
