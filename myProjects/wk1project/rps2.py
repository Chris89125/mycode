#!/usr/bin/python3

import random

def getUserName():

    print("welcome to Rock Paper Scissors")
    username=input("Please enter your name.\n")
    print("Hello ", username,"!",sep='') 
    return username


def getUserChoice():

    userChoice=input("Please Type R for Rock, P for Paper or S for Scissors\n")

    if userChoice.upper()=="R":
        print("You chose Rock!")
    elif userChoice.upper()=="P":
        print("You chose Paper!")
    elif userChoice.upper()=="S":
        print("You chose Scissors!")
    else:
        print("Not a good choice. Next time please choose R, P or S.")
        exit()

    print()
    return userChoice.upper()


def getCpuChoice():

    rpsChoices=["R","P","S"]
    cpuChoice=random.choice(rpsChoices)
    print("The CPU chose ", cpuChoice,"!\n",sep='')
    return cpuChoice


def compChoice(userChoice,cpuChoice):

    if userChoice.upper()==cpuChoice:
        print("You tied try again!")

    elif userChoice.upper()=="P":
        if cpuChoice=="R":
            print("You Win!")
        else: 
            print("You Lose!")

    elif userChoice.upper()=="R":
        if cpuChoice=="S":
            print("You Win!")
        else:
            print("You Lose!")

    elif userChoice.upper()=="S":
        if cpuChoice=="R":
            print("You Lose!")
        else: 
            print("You Win!")

    else:
        print("Not a good choice. Next time please choose R, P or S.")
        exit()
   



def main():
    username=getUserName()
    userChoice=getUserChoice()
    cpuChoice=getCpuChoice()
    compChoice(userChoice,cpuChoice)

    print("\nThanks for Playing ",username,"!",sep='')


if __name__ == "__main__":
    main()
    
