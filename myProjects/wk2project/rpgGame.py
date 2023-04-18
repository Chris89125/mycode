#!/usr/bin/python3
"""Role Playing game week 2 project"""

import random


VALID_ROOMS = ["GUARD_ROOM", "SCIENCE_LAB", "PUMP_ROOM", "ARMORY" ]
VALID_CMDS = ["I", "LOOK", "Q"]
VALID_DIRS = ["D", "U", "E", "W"]
VALID_ITEMS = ["KEY_CARD", "TERMINAL"]


inventory = [] 

def configureRooms():
    """Defining rooms"""
    rooms = \
        {
            "Guard_Room" : {
                "D" : "Science_Lab"
            },
            "Science_Lab" : {
                "U" : "Guard_Room",
                "D" : "Pump_Room"
            },
            "Pump_Room" : {
                "U" : "Science_Lab",
                "E" : "Armory"
            },
            "Armory" : {
                "W" : "Pump_Room"
            }
        }
    return rooms

def show_status(current_room,inventory):
    print(current_room)
    print(inventory)


def main():
    print("in main")

    print("inventory", inventory)

    rooms = configureRooms()
    print("rooms", rooms)

    while True:

        move=""
        while move == "":
            move=input(". > ")

            move = move.upper().split(" ",1)
            print( move )
            if move[0] == "Q": 
                print("Goodbye Quitter")
                exit()


            if move[0] == "D":
                print("You Move dowm to the next room")
            
            if move[0] == "U":
                print("You Move up to the next room")

            if move[0] == "W":
                print("You Move West to the next room")

            if move[0] == "E":
                print("You Move East to the next room")
                
                

if __name__ == "__main__":
    main()
