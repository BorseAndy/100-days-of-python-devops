import art, random

COUNTER_EASY_LEVEL = 10
COUNTER_HARD_LEVEL = 5

# Printing logo and a welcome message
print(art.logo)
print("Welcome to the Number Guessing Game!")

# Choosing a random number between 1 and 100.
min_number = 1
max_number = 100
random_number = random.randint(min_number,max_number)
# Function to set difficulty
def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return COUNTER_EASY_LEVEL
    elif level == "hard":
        return COUNTER_HARD_LEVEL
    else:
        print("There might be a typo!!\nWe didn't recognize your input.\nYou must enter 'easy' or 'hard'!")
        return 0

# Function to let the user guess a number
def check_answer():
    global random_number
    global counter_tries
    guess_number = int(input("Make a guess: "))
    if guess_number < random_number:
        print("Too low.\nGuess again.")
    elif guess_number > random_number:
        print("Too high.\nGuess again.")

    counter_tries -= 1

    if guess_number == random_number:
        print(f"You got it! The answer was {random_number}")
        counter_tries = 0

# Print the number range
print(f"I'm thinking of a number between {min_number} and {max_number}.")
# Set counter tries depending on difficulty level
difficulty = ""
counter_tries = set_difficulty()

# if difficulty == "easy":
#     counter_tries = 10
# elif difficulty == "hard":
#     counter_tries = 5
# else:
#     print("There might be a typo!!\nWe didn't recognize your input.\nYou must enter 'easy' or 'hard'!")

# Make a guess until tries = 0
while counter_tries != 0:
    print(f"You have {counter_tries} attempts remaining to guess the number")
    check_answer()