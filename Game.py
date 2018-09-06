# BattleShip
# Author: Vu Tran
from Board import *
from random import randint
from Validator import *
from Ship import *
"""This module is where all the game logic is stored,
from user input handling, turn management, winning condition testing"""


# Function to get ship's orientation
def orientation_selection():
    # This loop will continue until user selects the valid choices
    while True:
        # Stores user input as a string
        orientation_choice = input("Vertical or Horizontal? V or H\n")
        # Input validation, we will make this case insensitive
        if orientation_choice == "V" or orientation_choice == "H" or orientation_choice == "h" or \
                orientation_choice == "v":
            # return the valid input and ends the loop
            return orientation_choice
        # If input invalid will restart the loop
        else:
            print("Orientation must be an alphabetic character of V or H")


# Function to get coordinates, this function will be called to place ships and attack enemy ships
def get_coordinates():
    # Infinite loop, user must enter valid values before continuing
    while True:
        # Try block to catch exceptions
        try:
            # Saving the user input as a three character numeric string with a comma in between
            user_input = input("Enter the coordinates: x, y with a comma\n")
            # Removes the comma and stores the value in the coordinates string
            coordinates = user_input.split(",")
            # Convert the coordinates to int and store them in a list
            int_coordinates = list(map(int, coordinates))
            # If user entered any more or less characters, an exception will be raised
            if len(int_coordinates) != 2:
                raise Exception("Invalid entry! make sure there is there are two values separated by a comma")
            # Since the indexes always that 0, anything user inputs will be index[x] - 1
            int_coordinates[0] = int_coordinates[0] - 1
            int_coordinates[1] = int_coordinates[1] - 1
            # If user enters any coordinates > 10 or < 0, a new exception will be raised
            if int_coordinates[0] > 9 or int_coordinates[0] < 0 or 9 < int_coordinates[1] < 0:
                raise Exception("Coordinates values must be between 1 and 10!")
            # Return the coordinates if everything checks out
            return int_coordinates
        # Catches the ValueError, in case the user tries to enter "one, five" as coordinates, input must be a numeric
        # string
        except ValueError:
            print("Coordinates must be numerals!")
        # Catches all the previously raised exceptions
        except Exception as e:
            print(e)


# Function to place the ship, this function takes the board, ship, player marker, orientation, and coordinates as
# parameters
def place_ship(board, ship, p, orientation, x, y):
    # Place ship based on orientation,  if vertical the x will be incremented, if horizontal the y will be incremented
    if orientation == "V" or orientation == "v":
        for i in range(ship):
            board[x + i][y] = p
    elif orientation == "H" or orientation == "h":
        for i in range(ship):
            board[x][y + i] = p
    # return the updated board
    return board


# Function to place player's ships, takes the current board and ships and parameters
def player_place_ship(board, ships):
    # Loop through the ships dictionary keys, the keys are ship names, the values are the ship sizes, The loop will \
    # iterate through to place every ship in the dictionary.
    for ship in ships.keys():
        """
        Set the valid boolean to false, since it's possible to pass all the validations and have a ship that
        intersects with another ship or goes off the board, this function prevents this from happening, 
        The loop is infinite, until a successful placement occurs
        """
        valid = False
        while not valid:
            # Display the most current player's board with all the previous placements
            display_board("p", board)
            # Output to let player know which ship is being placed and how many blocks the ship will occupy
            print("Placing a/an " + ship)
            print(ship + " take up " + str(ships[ship]) + " blocks")
            # Prompts the user for coordinates input, this is important since it's the point of origin for the ship,
            # and the x or y will increment depending on orientation selection
            print("Enter the origin point of your ship")
            # Get coordinates input
            x, y = get_coordinates()
            # Get orientation selection
            orientation = orientation_selection()
            # The acceptable_placement function in the Validator module, checks for valid placement to make sure the \
            # the ship is not placed out of bounds of the board. The function returns a boolean.
            valid = acceptable_placement(board, ships[ship], x, y, orientation)
            # If not valid, prompt the user to input the return key to start the loop again
            if not valid:
                print("Cannot place a ship there.\nTry again.")
                input("Hit RETURN/ENTER to continue")

        # If acceptable_placement returned true, break out of the loop and updates the board with placed ship
        board = place_ship(board, ships[ship], ship[0], orientation, x, y)
        # Display the updated board with ship place
        display_board("p", board)
    # At the end of the for loop, after all the valid ship placements we prompt the user to input the return key to
    # Start turn
    input("Done placing player ships. Hit ENTER to continue")
    # return updated board
    return board


# Function to get the computer to place ships
def computer_place_ships(board, ships):
    # Loop through the ship dictionary for each individual key
    for ship in ships.keys():
        # Valid set to false until the condition is true
        valid = False
        # Infinite loop
        while not valid:
            # random x, and y coordinates
            x = randint(1, 10) - 1
            y = randint(1, 10) - 1
            # random orientation selection
            o = randint(0, 1)
            if o == 0:
                orientation = "V"
            else:
                orientation = "H"
            # Checks to see if the randomly generated coordinates and orientation are valid to place on board
            valid = acceptable_placement(board, ships[ship], x, y, orientation)

        # If valid break out of the while loop and place ship
        print("Computer placing a/an " + ship)
        board = place_ship(board, ships[ship], ship[0], orientation, x, y)
    # return updated board
    return board


# Function to attack enemy ships, returns response
def fire(board, x, y):
    # Make a move on the board and return the result, hit, miss or try again for repeat hit
    # If attack coordinates are on empty x and y index return miss
    if board[x][y] == -1:
        return "******* MISS! *******"
    # If attack coordinates already played, prompt the user to re-try
    elif board[x][y] == "X" or board[x][y] == "*":
        return "Try AGAIN"
    # else on occupied index, return hit
    else:
        return "******* Hit! ********"


# Function to start player's turn
def player_turn(board):
    # Get coordinates from the user and try to make move
    # If attack is a hit, check ship_status and win condition
    while True:
        print("Select coordinate to attack")
        # Get attack coordinates
        x, y = get_coordinates()
        # Input validation, coordinates for both x and y must be between 1 and 10
        if x > 10 or x < 0 or y > 10 or y < 0:
            print("Coordinates for both x and y must be between 1 and 10. Try again")
        else:
            # Get response
            response = fire(board, x, y)
            # If response is hit
            if response == "******* Hit! ********":
                # Display response and coordinates of the hit
                print(response)
                print("Hit at " + str(x + 1) + "," + str(y + 1))
                # Checks the ship's status, if ship is sunk display in console
                check_ship_status(board, x, y)
                # Mark the coordinate with an X on the board
                board[x][y] = "X"
                # Check if that was the winning move
                if get_turn_winner(board):
                    return "WINNER!"
            # If response is a miss
            elif response == "******* MISS! *******":
                # Display response and miss coordinates
                print(response)
                print(str(x + 1) + "," + str(y + 1) + " is a miss.")
                # Mark the miss coordinate on the board
                board[x][y] = "*"
            # This response is returned when user inputs a coordinate that already has value in it
            elif response == "TRY AGAIN":
                print("That coordinate was already hit. Try again")

            if response != "TRY AGAIN":
                # Return the updated board
                return board


def computer_turn(board):
    # Generate user coordinates from the user and try to make move
    # If move is a hit, check ship sunk and win condition
    while True:
        # Randomly generate x and y coordinates
        x = randint(1, 10) - 1
        y = randint(1, 10) - 1
        # Get response from coordinates
        response = fire(board, x, y)
        # If response is hit
        if response == "******* Hit! ********":
            # Display response and hit coordinates
            print(response)
            print("Hit at " + str(x + 1) + "," + str(y + 1))
            # Check the ship status
            check_ship_status(board, x, y)
            # Mark the x and y index with X
            board[x][y] = 'X'
            # Check winning conditions
            if get_turn_winner(board):
                return "WINNER!"
        # If response is a miss
        elif response == "******* MISS! *******":
            # Display response and coordinates of the miss
            print(response)
            print(str(x + 1) + "," + str(y + 1) + " is a miss.")
            # Mark the coordinates with a *
            board[x][y] = "*"

        if response != "TRY AGAIN":
            return board


# Function to check which ship was hit, if the string character on the board matches
# then display ship
def check_ship_status(board, x, y):
    ships = assign_ships()
    for i in ships.keys():
        ship = i
    # figure out what ship was hit
    if board[x][y] == "A":
        ship = "Aircraft Carrier"
    elif board[x][y] == "B":
        ship = "Battleship"
    elif board[x][y] == "S":
        ship = "Submarine"
    elif board[x][y] == "D":
        ship = "Destroyer"
    elif board[x][y] == "P":
        ship = "Patrol Boat"

    # mark cell as hit and check if sunk
    board[-1][ship] -= 1
    # If ship is empty then it is sunk
    if board[-1][ship] == 0:
        print(ship + " SUNK")


# Function to check if the last move made resulted in a winner
def get_turn_winner(board):
    # simple for loop to check all cells in 2d board
    # if any cell contains a char that is not a hit or a miss return false
    for i in range(10):
        for j in range(10):
            if board[i][j] != -1 and board[i][j] != "*" and board[i][j] != "X":
                return False
    return True



