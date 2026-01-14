import art, random

#-----Function------
def add(number1, number2):
    return number1 + number2

def deal_card():
    """ Return a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list_cards):
    """ Take a list of cards and return the score calculated from the cards.
        0 ---> Blackjack
        sum >24 and 11 is available ---> 11 will be replaced with 1"""
    if sum(list_cards) == 21 and len(list_cards) == 2:
        return 0 # 0 means Blackjack

    if 11 in list_cards and sum(list_cards) > 21:
        list_cards.remove(11)
        list_cards.append(1)

    return sum(list_cards)

# def draw_cards():
#     user_number.append(deal_card())
#     pc_number.append(deal_card())
#
# def draw_card_pc():
#     pc_number.append(deal_card())
#
# def draw_card_user():
#     user_number.append(deal_card())

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose!❌ opponent has a Blackjack"
    elif user_score == 0:
        return "You Win with Blackjack!🏁"
    elif user_score > 21:
        return "You lose because you went over 21!❌"
    elif computer_score >21:
        return "You Win because PC went over 21!🏁"
    elif user_score > computer_score:
            return "You win 😁"
    else:
            return "You lose 😤"

def play_game():
    ###-----Main Program-----
    #----- Variables------
    user_number = []
    pc_number = []
    score_pc = -1
    score_user = -1
    is_game_over = False
    print(art.logo)
    for _ in range (2):
        user_number.append(deal_card())
        pc_number.append(deal_card())
    while not is_game_over:
        score_user = calculate_score(user_number)
        score_pc = calculate_score(pc_number)
        print(f"Your cards: {user_number}, current score: {score_user}")
        print(f"Computer's first card: {pc_number[0]}")

        if score_user == 0 or score_pc == 0 or score_user > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_number.append(deal_card())
            else:
                is_game_over=True

    while score_pc !=0 and score_pc < 17:
        pc_number.append(deal_card())
        score_pc = calculate_score(pc_number)

    print(f"Your final hand: {user_number}, final score: {score_user}")
    print(f"Computer's final hand: {pc_number}, final score: {score_pc}")
    print(compare(score_user, score_pc))

while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == "y":
    play_game()