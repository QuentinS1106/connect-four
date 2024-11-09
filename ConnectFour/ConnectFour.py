# This represents a board with 7 columns, 6 rows each
# 0 represents an empty space, 1 is red, 2 is yellow
# In each column, the first index represents the bottom slot
board = [[0 for y in range(6)] for x in range(7)]

def place(player, col):
    """Places the specified player's piece into the bottom place in the specified column.
    
    Parameters:
        player: The player who's piece is being played. 1 is red, 2 is yellow
        col: The column to place the piece into, if possible

    Returns:
        Boolean: True if the move is possible, False if the move is not possible (the column is full)
    """
    global board
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
    
def printBoard():
    '''Prints out a representation of the board.'''
    global board
    result = ''
    # board goes from bottom to top, so printing from top to bottom requires iterating though board backwards
    for y in range(5,-1,-1):
        for x in range(7):
            result += str(board[x][y]) + ' '
        result += '\n'
    print(result)

def checkWin():
    '''Checks if either player has four of their pieces in a row.
    
    Returns:
        Boolean: True if the board has a four in a row, False otherwise'''
    # Check for horizontal four in a rows.
    for y in range(6):
        for x in range(4):
            if (0 != board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y]):
                return True
    # Check for vertical four in a rows.
    for x in range(7):
        for y in range(3):
            if (0 != board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3]):
                return True
    # Check for top-left to bottom-right four in a rows.
    for x in range(4):
        for y in range(3):
            if (0 != board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]):
                return True
    # Check for bottom-left to top-right four in a rows.
    for x in range(4):
        for y in range(5,2,-1):
            if (0 != board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3]):
                return True
    return False
