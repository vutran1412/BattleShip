# BattleShip
# Author: Vu Tran
from Game import *
from copy import *
from Ship import *
"""Based on the rules of the original battle ship game
https://en.wikipedia.org/wiki/Battleship_(game)
Learned about how to deep copy an object and all of its elements from 
https://stackoverflow.com/questions/184710/what-is-the-difference-between-a-deep-copy-and-a-shallow-copy"""


# Main Function, called to play the game
def main():
    # An empty board is built
    new_board = build_board()
    # Creates a dictionary containing ship name as key and ship size as value
    ships = assign_ships()
    # From the empty new board, we create copies using deepcopy, the object and all the elements are
    # copied, we do this so we don't have to recreate a 2d list and redraw the grid
    computer_board = deepcopy(new_board)
    player_board = deepcopy(new_board)

    # Append the ship dictionary as the last index of the board list
    computer_board.append(deepcopy(ships))
    player_board.append(deepcopy(ships))

    # Set up the game and place the ships
    computer_board = computer_place_ships(computer_board, ships)
    player_board = player_place_ship(player_board, ships)

    # Main game loop, will run as long as no winner is decided
    while 1:
        # Player's turn
        # displays the computer's board
        display_board("c", computer_board)
        # interact with the board by inputting attack coordinates
        computer_board = player_turn(computer_board)

        # Checks if player is winner
        if computer_board == "WINNER!":
            print("You WIN!\n")
            quit()

        # Display the current computer board
        display_board("c", computer_board)
        input("To end player turn hit ENTER")

        # computer move
        player_board = computer_turn(player_board)

        # check if computer move
        if player_board == "WINNER!":
            print("Computer WINS! You Lost!")
            quit()

        # display user board
        display_board("p", player_board)
        input("To end computer turn hit ENTER")


main()
