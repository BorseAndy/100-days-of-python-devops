MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Define coins as a constant variable
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01

def ask_user():
    """Ask user what he would like and return it"""
    return str(input("What would you like? (espresso/latte/cappuccino): ").lower())

def print_report():
    """When this function is called a report of Machine will be printed"""
    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]
    money_available = resources["money"]
    print(f"Water: {water_available}")
    print(f"Milk: {milk_available}")
    print(f"Coffee: {coffee_available}")
    print(f"Money: {money_available}")


def check_resources(user_choice):
    """Check if the machine have enough resources to make the coffe"""
    water_needed= 0
    coffee_needed = 0
    milk_needed = 0

    if user_choice == "espresso":
        water_needed = MENU[user_choice]["ingredients"]["water"]
        coffee_needed = MENU[user_choice]["ingredients"]["coffee"]
        print(f"Water need: {water_needed}; Coffee needed: {coffee_needed}")
    elif user_choice != "espresso":
        water_needed = MENU[user_choice]["ingredients"]["water"]
        coffee_needed = MENU[user_choice]["ingredients"]["coffee"]
        milk_needed = MENU[user_choice]["ingredients"]["milk"]
        print(f"Water need: {water_needed}\nCoffee needed: {coffee_needed}\nMilk needed: {milk_needed}")

    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]
    if water_available < water_needed:
        print("Sorry there is not enough water!")
        return False
    if coffee_available < coffee_needed:
        print("Sorry there is not enough coffee!")
        return False
    if milk_available < milk_needed:
        print("Sorry there is not enough milk!")
        return False
    return True

def ask_for_coins(initial_money, user_choice):
    user_money =  initial_money
    money_needed = MENU[user_choice]["cost"]
    print(f"Please insert coins. Money needed ${money_needed}")
    amount_quarters = float(input("How many quarters?: "))
    user_money += (amount_quarters * QUARTERS)
    print(f"{amount_quarters} * {QUARTERS} + {user_money} = {user_money}")
    amount_dimes = float(input("How many dimes?: "))
    user_money += (amount_dimes * DIMES)
    print(f"{amount_dimes} * {DIMES} = {user_money}")
    amount_nickles = float(input("How many nickles?: "))
    user_money += (amount_nickles * NICKLES)
    print(f"{amount_nickles} * {NICKLES} = {user_money}")
    amount_pennies = float(input("How many pennies?: "))
    user_money += (amount_pennies * PENNIES)
    print(f"{amount_pennies} * {PENNIES} = {user_money}")
    return user_money

def subtract_resources(coffee_choice):
    water_needed = MENU[coffee_choice]["ingredients"]["water"]
    coffee_needed = MENU[coffee_choice]["ingredients"]["coffee"]
    milk_needed = MENU[coffee_choice]["ingredients"]["milk"]
    print(f"Before {resources}")
    if user_choice == "espresso":
        resources["water"] -= water_needed
        resources["coffee"] -= coffee_needed
    elif user_choice != "espresso":
        resources["water"] -= water_needed
        resources["coffee"] -= coffee_needed
        resources["milk"] -= milk_needed
    print(f"After {resources}")

# TODO: Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def check_transaction(user_choice):
    user_money= 0
    money_available = resources["money"]
    user_money += money_available
    money_needed = MENU[user_choice]["cost"]
    if money_available < money_needed:
        user_money = ask_for_coins(user_money, user_choice)
    if user_money >= money_needed:
        return True
    else:
        return False

def make_coffee():
    return print("Here is you coffee")

Machine_ready= True
resources["money"] = 0

print(resources)

# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


while not Machine_ready == False:
    user_choice = ask_user()
# TODO: Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice == "off":
        Machine_ready = False

# TODO: Print report. -> a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.

    if user_choice == "report":
        print_report()
    for i in MENU.keys():
        if user_choice == i:
            # TODO: Check resources sufficient?
            if check_resources(user_choice):
                # TODO: Check transaction successful?
                if check_transaction(user_choice):
                    # TODO: Make Coffee.
                    make_coffee()
                    subtract_resources(user_choice)
                else:
                    print("Sorry that's not enough money. Money refunded.")


# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.