import os

# Globally define the board we are playing on.
Gameboard = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Terminal width for centering the playing board
TermWidth = os.get_terminal_size().columns

# Check if there is a winner.
def CheckWinner(CurrentGame):
    # Winning Triples
    Xwins = ['X','X','X']
    Owins = ['O','O','O']

    # Check rows
    for i in CurrentGame:
        if i == Xwins:
            return 'X wins'
        if i == Owins:
            return 'O wins'

    # Check Columns
    for col in range(len(CurrentGame)):
        ThreeCheck = [CurrentGame[row][col] for row in range(len(CurrentGame))]
        if ThreeCheck == Xwins:
            return 'X wins'
        if ThreeCheck == Owins:
            return 'O wins'

    # Check Diagonals
    # Forward Diagonal
    ForwardDiag = [CurrentGame[0][0], CurrentGame[1][1], CurrentGame[2][2]]
    if ForwardDiag == Xwins:
        return 'X wins'
    if ForwardDiag == Owins:
        return 'O wins'
    # Backwards Diagonal
    BackDiag = [CurrentGame[0][2], CurrentGame[1][1], CurrentGame[2][0]]
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
            print('---|---|---'.center(TermWidth))
    print('')

# Get a valid input.  Takes in what round we are on, and returns the row and column the user inputs
def GetInput(round):
    while True:
            try:
                if round%2 == 0:
                    print('Player X, please choose your location.')
                else:
                    print('Player O, please choose your location.')
                moveRow = int(input("Please enter the row of your next move (0,1, or 2): "))
                moveCol = int(input("Please enter the column of your next move (0,1, or 2): "))
                break
            except:
                print('')
                print("Not a valid number.  Please enter a valid number.")
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