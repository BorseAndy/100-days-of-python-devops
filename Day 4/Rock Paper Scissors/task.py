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

random_number_from_pc = random.randint(0,2)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

elements = [rock, paper, scissors]
# print(f"PC random number is: {random_number_from_pc} {elements[random_number_from_pc]}")
# print(f"User input is: {user_input}")

if user_input == 2 and random_number_from_pc==0:
    print(f"You choose {user_input}\n {elements[user_input]}")
    print(f"PC choose {random_number_from_pc}\n and YOU WIN with:  {elements[random_number_from_pc]}")
elif (user_input + 1) == random_number_from_pc:
    print(f"You choose {user_input}\n {elements[user_input]}")
    print(f"PC choose {random_number_from_pc}\n and YOU WIN with:  {elements[random_number_from_pc]}")
elif user_input == random_number_from_pc:
    print(f"You choose {user_input}\n {elements[user_input]}")
    print(f"PC choose {random_number_from_pc}\n and NOBODY WINS, restart")
else:
    print(f"You choose {user_input}\n {elements[user_input]}")
    print(f"PC choose and YOU LOSE with: {random_number_from_pc}\n {elements[random_number_from_pc]}")