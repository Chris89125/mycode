#!/usr/bin/python3

import random


print("welcome to Rock Paper Scissors")
username=input("Please enter your name.\n")
print("Hello ", username,"!",sep='') 

player=input("Please Type R for Rock, P for Paper or S for Scissors\n")

if player=="r" or player=="R":
   print("You chose Rock!")
elif player=="p" or player=="P":
   print("You chose Paper!")
elif player=="s" or player=="S":
   print("You chose Scissors!")
else:
    print("Not a good choice. Next time please choose R, P or S.")
    exit()
   
rpsChoices=["Rock!","Paper!","Scissors!"]
cpuChoice=random.choice(rpsChoices)
print("The CPU chose ", cpuChoice)

print("Thanks for Playing ",username,"!",sep='')

