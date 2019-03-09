from random import randint
from time import sleep

dicenum = randint(1, 6)

print("Rolling dice...")
print("")
print("    _______       \n  /\       \           \n /()\   ()  \          \n/    \_______\         \n\    /()     /         \n \()/   ()  /          \n  \/_____()/")
print("")

sleep(1)

if dicenum == 1:
          print(" _______\n|       |\n|   .   |\n|       |\n|_______|")
elif dicenum == 2:
          print(" _______\n| .     |\n|       |\n|     . |\n|_______|\n")
elif dicenum == 3:
          print(" _______\n| .     |\n|   .   |\n|     . |\n|_______|\n")
elif dicenum == 4:
          print(" _______\n| .   . |\n|       |\n| .   . |\n|_______|\n")
elif dicenum == 5:
          print(" _______\n| .   . |\n|   .   |\n| .   . |\n|_______|\n")
elif dicenum == 6:
          print(" _______\n| .   . |\n| .   . |\n| .   . |\n|_______|\n")

print("\nThe number is: " + str(dicenum))