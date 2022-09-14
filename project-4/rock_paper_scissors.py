import random

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

options = [rock, paper, scissors]

player_choice = int(input("Please inter your choose : (Type 0 fro Rock, 1 for Paper, 2 fro Scissors)\n"))

if player_choice >= 3 or player_choice < 0:
    print("Please enter a valid number, you lose!")
else:    
    print("player choice : ", options[player_choice])
    computer_choice = random.randint(0,2)
    print("computer choice : ", options[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("Hooray You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("Oooops You lose!")
    elif computer_choice > player_choice:
        print("Oooops You lose!")
    elif player_choice > computer_choice:        
        print("Hooray You Win!")
    elif player_choice == computer_choice:    
        print("It's a draw.")