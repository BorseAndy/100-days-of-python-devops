#from 'filename.py' import 'class'
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


Menu = Menu()
MoneyMachine = MoneyMachine()
CoffeMaker = CoffeeMaker()

machine_on = True
# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
while machine_on:
    user_choice = input(f"What would you like {Menu.get_items()}?: ")
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        CoffeMaker.report()
        MoneyMachine.report()
    else:
        #TODO: Check resources sufficient?)
        drink = Menu.find_drink(user_choice)
        if CoffeMaker.is_resource_sufficient(drink):
            # TODO: Process coins.
            if MoneyMachine.make_payment(drink.cost):
                CoffeMaker.make_coffee(drink)
