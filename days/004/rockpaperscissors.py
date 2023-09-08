import random as rand

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. \n"))

if user_choice > len(game_images) - 1:
    print("Number too large.")
    exit()
elif user_choice < 0:
    print("Number too small.")
    exit()
else:
    print(game_images[user_choice])
    
comp_choice = rand.randint(0,2)
print(f"Computer chose: {game_images[comp_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and comp_choice == 2:
    print("You Win!")
elif comp_choice == 0 and user_choice == 2:
    print("You Lose")
elif comp_choice > user_choice:
    print("You Lose")
elif user_choice > comp_choice:
    print("You Win")
elif comp_choice == user_choice:
    print("Its a draw")





