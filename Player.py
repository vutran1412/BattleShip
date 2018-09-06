# BattleShip
# Author: Vu Tran
# This module was created to store the player marker, but will be modified into a player class
# in the future for version 2.0, which will have player to player functionality


def get_player(p):
    player = ""
    if p == "p":
        player = "Player 1"
    elif p == "c":
        player = "Computer"
    return player
