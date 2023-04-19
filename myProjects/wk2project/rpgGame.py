#!/usr/bin/python3
"""Role Playing game week 2 project"""

import random

"""Global Variables to help validate logic"""
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

def show_status(rooms,current_room,inventory):
    """Display possiable player moves"""
    print(" Current Room:",current_room)
   # print("   From here you can ",rooms[current_room])

    print("   From here you can type...")
    if "U" in rooms[current_room]:
        print("    U to go to the",rooms[current_room]["U"])
    if "D" in rooms[current_room]:
        print("    D to go to the",rooms[current_room]["D"])
    if "E" in rooms[current_room]:
        print("    E to go to the",rooms[current_room]["E"])
    if "W" in rooms[current_room]:
        print("    W to go to the",rooms[current_room]["W"])

    if current_room=="Armory":
        print("You found the missing villager")
        print("You Win, Game Over!")
        exit()


def main():
    print("in main")

    inventory = [] 

    """Player Spawns in the Guard Room"""
    current_room="Guard_Room"

    """Set up the base room config"""
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
                print("You Quit like a Quitter")
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

                if valid_move:
                    show_status(rooms,current_room,inventory)
                else:
                    print("Invalid Move")
                

if __name__ == "__main__":
    main()
