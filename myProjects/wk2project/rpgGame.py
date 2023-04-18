#!/usr/bin/python3
"""Role Playing game week 2 project"""

import random

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


def main():
    print("in main")

    print("inventory", inventory)
    rooms = configureRooms()
    print("rooms", rooms)

if __name__ == "__main__":
    main()
