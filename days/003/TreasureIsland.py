print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
decisionOne = input("Welcome to Treasure Island \nYour mission is to find the treasure. \nYou\'re at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()

if decisionOne == "right":
    # Continue the game
    decisionTwo = input("You have come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if(decisionTwo == "wait"):
        decisionThree = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n').lower()
        if(decisionThree == "yellow"):
            print("Did you think yellow was for gold? Although you have found some cuddly cats. You approach them, and they claw your eyes out. Game Over.")  
        elif(decisionThree == "blue"):
            print("You found the treasure! You Win!")
        elif(decisionThree == "red"):
            print("Really the red one? Don't you know thats the color of blood? LOOK OUT BEHIND YOU! Game Over.")
        else:
            print("That door does not exist. Game Over.")
    else:
        print("You got eaten by a shark. Why would you swim? You could see the shark fins! Game Over.")
        exit()
elif decisionOne == "left":
    print("You fell into a bottomless pit. You fall until you grow old and die. Game Over.")
else:
    exit()