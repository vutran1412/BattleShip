# BattleShip
# Author: Vu Tran
"""This Module contains the functions to create and display the board that will be
used in the game"""
from Player import get_player


# Function to build the board a 10 x 10 2d list
def build_board():
    board = []
    for i in range(10):
        board_row = []
        for j in range(10):
            board_row.append(-1)
        board.append(board_row)
    return board


# Function to display the elements of the board
# Designed by Captain DeadBones
# https://github.com/ActiveState/code/tree/master/recipes/Python/578836_Game_Battleships/
def display_board(p, board):
    # Get player markers for the board
    player = get_player(p)
    print(player + "'s board:")
    # print the horizontal numbers
    # By specifying the end parameter to an empty space, subsequent print statements will display on the
    # same lin instead of a new line, since \n is the default value of the end parameter
    print(" ", end=" ")
    # this look prints all the horizontal line numbers and displays them on the same line, separated by a space
    for x in range(10):
        print("  " + str(x + 1) + "  ", end=" ")
    print("\n")

    # Outside for loop to iterate through the outside of the list
    for x in range(10):

        # Print the vertical line number
        # If the index is not equal to 9 then double space else single space
        if x != 9:
            print(str(x + 1) + "  ", end=" ")
        else:
            print(str(x + 1) + " ", end=" ")

        # print the board values, and cell dividers, because of the end parameter, \
        # everything gets printed on the same line
        for y in range(10):
            # If its empty, then will contain an empty space
            if board[x][y] == -1:
                print(" ", end=" ")
            # If player marker is player, then display the current board values, ships, hits, and misses
            elif p == "p":
                print(board[x][y], end=" ")
            # If player marker is computer, then display the hits and the misses on the board
            elif p == "c":
                if board[x][y] == "*" or board[x][y] == "X":
                    print(board[x][y], end=' ')
                else:
                    print(" ", end=' ')
            # If any index is not equal to 9 then display a pipe as separator
            if y != 9:
                print(" | ", end=' ')
        print()
        # print a horizontal line
        if x != 9:
            print("   ----------------------------------------------------------")
        else:
            print()













