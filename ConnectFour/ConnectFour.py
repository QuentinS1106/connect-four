def createBoard(x=7, y=6):
    '''Creates a Connect Four board. By default, this board has 7 columns and 6 rows.
    The number of columns and rows can be altered by changing x and y.
    
    Parameters:
        x: The desired number of columns for the board to have, default is 7. x > 0
        y: The desired number of rows for the board to have, default is 6. y > 0
    '''
    # This represents a board with x columns, y rows each
    # 0 represents an empty space, other integers represent the player who's piece is in that space
    # In each column, the first index represents the bottom slot
    return [[0 for n in range(y)] for m in range(x)]

def place(player, col, board):
    '''Places the specified player's piece into the bottom place in the specified column.
    
    Parameters:
        player: The player who's piece is being played.
        col: The column to place the piece into, if possible

    Returns:
        Boolean: True if the move is possible, False if the move is not possible (the column is full)
    '''
    # Checks if the top space in the column is full. If it is, the move cannot be made.
    # This also prevents an indexing error when iterating through the column later.
    if board[col][-1] != 0:
        return False
    else:
        # Look for the bottommost empty space in the list.
        # Since the top space is empty, this has to eventually find an empty space.
        # Therefore, this has to terminate before passing the end of the list, preventing an error.
        y = 0
        while (board[col][y] != 0):
            y += 1
        board[col][y] = player
        return True
    
def printBoard(board):
    '''Prints out a representation of the board.'''
    result = ''
    # board goes from bottom to top, so printing from top to bottom requires iterating though board backwards
    for y in range(len(board[0]) - 1,-1,-1):
        for x in range(len(board)):
            result += str(board[x][y]) + ' '
        result += '\n'
    print(result)

def checkWin(board):
    '''Checks if either player has four of their pieces in a row.
    
    Returns:
        Boolean: True if the board has a four in a row, False otherwise
    '''
    # Check for horizontal four in a rows.
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if (0 != board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y]):
                return True
    # Check for vertical four in a rows.
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if (0 != board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3]):
                return True
    # Check for top-left to bottom-right four in a rows.
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if (0 != board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]):
                return True
    # Check for bottom-left to top-right four in a rows.
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 1,2,-1):
            if (0 != board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3]):
                return True
    return False

def play(players = 2):
    '''Plays a game of Connect Four
    
    Parameters:
        players: The number of players that will be playing. Default is 2. players > 0'''
    answer = ''
    while (answer != '0' and answer != '1'):
        answer = input('Enter 0 to play using the default board, or 1 to play using a custom board. ')
    if (answer == '0'):
        board = createBoard()
    else:
        while (True):
            try:
                cols = int(input('How many columns will the board have? '))
                break
            except:
                print('Please input a valid number.')
        while (True):
            try:
                rows = int(input('How many rows will the board have? '))
                break
            except:
                print('Please input a valid number.')
        board = createBoard(cols, rows)
    playing = -1
    while (not checkWin(board)):
        printBoard(board)
        playing = (playing + 1) % players
        column = -1
        while (type(column) != int or column < 1 or column > len(board)):
            column = input('Player {}, which column do you want to play in? (1-{}) '.format(playing+1, len(board)))
            try:
                column = int(column)
            except:
                print('Please input a valid number.')
        legalMove = False
        while (legalMove == False):
            legalMove = place(playing+1, column - 1, board)
            if (legalMove == False):
                column = -1
                while (type(column) != int or column < 1 or column > len(board)):
                    column = input('Please try again. ')
                    try:
                        column = int(column)
                    except:
                        print('Please input a valid number.')
    printBoard(board)
    print('Player {} is the winner!'.format(playing+1))

play()