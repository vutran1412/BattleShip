# BattleShip
# Author: Vu Tran
"""The Validator module validates user input,
The coordinates to place the ships must not over lap or
go outside of the board"""


# Function to verify placement of ship
def acceptable_placement(board, ship, x, y, orientation):
    # validate the ship can be placed at given coordinates
    if (orientation == "V" or orientation == "v") and x + ship > 10:
        return False
    elif (orientation == "H" or orientation == "h") and y + ship > 10:
        return False
    else:
        if orientation == "V" or orientation == "v":
            for i in range(0, ship):
                if board[x + i][y] != -1:
                    return False
        elif orientation == "H" or orientation == "h":
            for i in range(ship):
                if board[x][y + i] != -1:
                    return False

    return True
