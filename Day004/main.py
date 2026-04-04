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
    ________
---'   _____)_______
          ___________)
          _____________)
         ____________)
---.______________)
'''

scissors = '''
    ________
---'   _____)______
          __________)
       _______________)
      (____)
---.__(___)
'''

options = [rock,paper,scissors]

user_choice = int(input("Wanna play 🪨📄✂️? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_choice >= 0 and user_choice <= 2:
    if user_choice == 0:
        print("You choose: Rock")
    elif user_choice == 1:
        print("You choose: Paper")
    elif user_choice == 2:
        print("You choose: Scissors")
    print(options[user_choice])


computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer choose: Rock")
elif computer_choice == 1:
    print("Computer choose: Paper")
elif computer_choice == 2:
    print("Computer choose: Scissors")
print(options[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
