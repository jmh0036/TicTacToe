import os
import random

# Get input for how large a board to play on
Boardsize = 0
while Boardsize < 1:
    try:
        Boardsize = int(input('How large of a board would you like (positive integer)? '))
    except:
        print('')
        print('Not a valid integer.  Please enter an integer larger than 1.')

# Get input for the number of players
Players = 0
while Players != 1 and Players != 2:
    try:
        Players = int(input('How many players would you like to play (1 or 2)? '))
    except:
        print('')
        print('Not a valid input.  Please choose either 1 or 2 players.')

# Globally define the board we are playing on.
Gameboard = [[' ' for i in range(Boardsize)] for j in range(Boardsize)]

# Terminal width for centering the playing board
TermWidth = os.get_terminal_size().columns

# Check if there is a winner.
def CheckWinner(CurrentGame):
    Dimension = len(CurrentGame)

    # Winning Triples
    Xwins = ['X' for i in range(Dimension)]
    Owins = ['O' for i in range(Dimension)]

    # Check rows
    for i in CurrentGame:
        if i == Xwins:
            return 'X wins'
        if i == Owins:
            return 'O wins'

    # Check Columns
    for col in range(Dimension):
        ThreeCheck = [CurrentGame[row][col] for row in range(Dimension)]
        if ThreeCheck == Xwins:
            return 'X wins'
        if ThreeCheck == Owins:
            return 'O wins'

    # Check Diagonals
    # Forward Diagonal
    ForwardDiag = [CurrentGame[i][i] for i in range(Dimension)]
    if ForwardDiag == Xwins:
        return 'X wins'
    if ForwardDiag == Owins:
        return 'O wins'
    # Backwards Diagonal
    BackDiag = [CurrentGame[i][Dimension-i-1] for i in range(Dimension)]
    if BackDiag == Xwins:
        return 'X wins'
    if BackDiag == Owins:
        return 'O wins'

    # If nobody wins, return 'No Winner'
    return 'No Winner'

# Print the board out nicely
def PrintBoard(CurrentGame):
    print('')
    for i in range(len(CurrentGame)):
        row = ''
        for j in range(len(CurrentGame[i])):
            row += ' ' + str(CurrentGame[i][j]) + ' |'
        print(row[:-1].center(TermWidth))
        if i < (len(CurrentGame) - 1):
            Divisions = ''
            for j in range(len(CurrentGame)):
                Divisions += '---|'
            print(Divisions[:-1].center(TermWidth))
    print('')

# Get a valid input.  Takes in what round we are on, and returns the row and column the user inputs
def GetInput(round):
    # Set as empty for empty input
    moveRow = 'empty'
    moveCol = 'empty'
    # Two players no AI
    if Players == 2:
        # while there is no input (in case someone hits enter without inputting data)
        while moveRow == 'empty' or moveCol == 'empty':
            try:
                # Take turns
                if round%2 == 0:
                    print('Player X, please choose your location.')
                else:
                    print('Player O, please choose your location.')
                # Get move data
                moveRow = int(input('Please enter the row of your next move (from 0 to ' + str(len(Gameboard)-1) + '): ' ))
                moveCol = int(input('Please enter the column of your next move (from 0 to ' + str(len(Gameboard)-1) + '): ' ))
            except:
                print('')
                print('Not a valid number.  Please enter a valid number.')
                PrintBoard(Gameboard)
        return [moveRow, moveCol]
    # Single Player with AI
    else:
        # while there is no input (in case someone hits enter without inputting data)
        while moveRow == 'empty' or moveCol == 'empty':
            try:
                # Human's turn
                if round%2 == 0:
                    print('Player X, please choose your location.')
                    moveRow = int(input('Please enter the row of your next move (from 0 to ' + str(len(Gameboard)-1) + '): ' ))
                    moveCol = int(input('Please enter the column of your next move (from 0 to ' + str(len(Gameboard)-1) + '): ' ))
                # AI's turn
                else:
                    # BestMove will contain the smart move if one is available
                    BestMove = []

                    # If Odd size board, pick center if available
                    CenterSquare = (Boardsize-1)//2
                    if Boardsize%2 == 1 and Gameboard[CenterSquare][CenterSquare] == ' ':
                        moveRow = CenterSquare
                        moveCol = CenterSquare
                        BestMove = [CenterSquare, CenterSquare]
                    # Comb through the Game to see if the next move causes a win.
                    for nextmoverow in range(Boardsize):
                        for nextmovecol in range(Boardsize):
                            if Gameboard[nextmoverow][nextmovecol] == ' ':
                                # See if 'X' has a winning move
                                Gameboard[nextmoverow][nextmovecol] = 'X'
                                if CheckWinner(Gameboard) != 'No Winner':
                                    BestMove = [nextmoverow,nextmovecol]
                                # See if 'O' has a winning move
                                Gameboard[nextmoverow][nextmovecol] = 'O'
                                if CheckWinner(Gameboard) != 'No Winner':
                                    BestMove = [nextmoverow,nextmovecol]
                                # Be sure to clear out the pick that wasn't really made
                                Gameboard[nextmoverow][nextmovecol] = ' '
                    # No smart move
                    if BestMove == []:
                        moveRow = random.randint(0,Boardsize-1)
                        moveCol = random.randint(0,Boardsize-1)
                        print('The computer has chosen row', moveRow, 'column', moveCol)
                    # Choose the smart move
                    else:
                        moveRow = BestMove[0]
                        moveCol = BestMove[1]
                        print('The computer has chosen row', moveRow, 'column', moveCol)
            except:
                print('')
                print('Not a valid number.  Please enter a valid number.')
                PrintBoard(Gameboard)

        return [moveRow, moveCol]   

PrintBoard(Gameboard)

# Count the number of turns
turn = 0
# Keep playing until either there is a winner or every position has been played on
while (CheckWinner(Gameboard) == 'No Winner') and turn < len(Gameboard)**2:
    Input = GetInput(turn)
    # Make sure that the integer input is within our field of play (3 by 3)
    while Input[0] not in range(len(Gameboard)) or Input[1] not in range(len(Gameboard)):
        if Input[0] not in range(len(Gameboard)) and Input[1] not in range(len(Gameboard)):
            print('')
            print('Both Row and Column inputs are not a valid location.')
            PrintBoard(Gameboard)
        elif Input[0] not in range(len(Gameboard)):
            print('')
            print('Row input is not a valid location.')
            PrintBoard(Gameboard)
        else:
            print('')
            print('Column input is not a valid location.')
            PrintBoard(Gameboard)
        Input = GetInput(turn)

    # Make sure that the position is not already occupied
    while Gameboard[Input[0]][Input[1]] != ' ':
        print('')
        print('There is already a token in that location.  Please choose another location')
        PrintBoard(Gameboard)
        Input = GetInput(turn)
    
    # Alternate player's turn
    if turn%2 == 0:
        Gameboard[Input[0]][Input[1]] = 'X'
    else:
        Gameboard[Input[0]][Input[1]] = 'O'

    # Increment the turn by 1
    turn += 1

    PrintBoard(Gameboard)

# Return the winner!
print(CheckWinner(Gameboard))