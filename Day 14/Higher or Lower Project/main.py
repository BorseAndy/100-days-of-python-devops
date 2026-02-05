#import random module, art and game data
import random, art, game_data

score = 0
user_loses = False
print(art.logo)
Compare_A = []
Compare_B = []
user_input = ""

#function that choose randomly a data and returns the data
def randomize_object():
    rand_object = random.choice(game_data.data)
    return rand_object

#function that choose randomly a data and returns the data
def compare_object_equal():
    global Compare_A, Compare_B
    while Compare_A == Compare_B:
        Compare_A = random.choice(game_data.data)
        Compare_B = random.choice(game_data.data)

def print_compare_objects():
    global Compare_A, Compare_B, score
    if score > 0:
        print(art.logo)
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {Compare_A['name']}, a {Compare_A['description']}, from {Compare_A['country']}")
    print(art.vs)
    print(f"Compare B: {Compare_B['name']}, a {Compare_B['description']}, from {Compare_B['country']}")

def compare_object(input_from_user):
    global Compare_A, Compare_B, user_loses, score
    if Compare_A['follower_count'] >> Compare_B['follower_count'] and user_input == 'a':
        score += 1
        print("\n"*20)
    elif Compare_A['follower_count'] << Compare_B['follower_count'] and user_input == 'b':
        score += 1
        Compare_A = Compare_B
        print("\n" * 20)
    else:
        user_loses = True
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry that's wrong! Final score: {score}")


while user_loses == False:
    if score == 0:
      Compare_A = randomize_object()
    Compare_B = randomize_object()
    print_compare_objects()
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    while not (user_input == "a" or user_input == "b"):
        user_input = input("There might be a typo. You have to enter 'a' or 'b' to validate de input!\nWho has more followers? Type 'A' or 'B': ").lower()
    compare_object(user_input)
