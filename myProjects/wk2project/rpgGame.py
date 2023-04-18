#!/usr/bin/python3
"""Role Playing game week 2 project"""

import random


VALID_ROOMS = ["GUARD_ROOM", "SCIENCE_LAB", "PUMP_ROOM", "ARMORY" ]
VALID_CMDS = ["I", "LOOK", "Q"]
VALID_DIRS = ["D", "U", "E", "W"]
VALID_ITEMS = ["KEY_CARD", "TERMINAL"]



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

    inventory = [] 
    current_room="Guard_Room"

    print("inventory", inventory)

    rooms = configureRooms()
    print("rooms", rooms)

    while True:

        move=""
        while move == "":
            move=input(". > ")
            valid_move = False

            move = move.upper().split(" ",1)
            print( move )
            if move[0] == "Q": 
                print("Goodbye Quitter")
                exit()

            if move[0] in VALID_DIRS:  
                valid_move = True
                if move[0] == "D":
                    if move[0] in rooms[current_room]:
                        from_room=current_room
                        current_room=rooms[current_room][move[0]]
                        print(" You moved from:",from_room,"To:",current_room)
                    else:   
                        valid_move = False
                elif move[0] == "U":
                    if move[0] in rooms[current_room]:
                        from_room=current_room
                        current_room=rooms[current_room][move[0]]
                        print(" You moved from:",from_room,"To:",current_room)
                    else:   
                        valid_move = False
                elif move[0] == "E":
                    if move[0] in rooms[current_room]:
                        from_room=current_room
                        current_room=rooms[current_room][move[0]]
                        print(" You moved from:",from_room,"To:",current_room)
                    else:   
                        valid_move = False
                elif move[0] == "W":
                    if move[0] in rooms[current_room]:
                        from_room=current_room
                        current_room=rooms[current_room][move[0]]
                        print(" You moved from:",from_room,"To:",current_room)
                    else:   
                        valid_move = False
                else:   
                    print("Invalid Move")

                if not valid_move:
                    print("Invalid Move")
                

if __name__ == "__main__":
    main()
