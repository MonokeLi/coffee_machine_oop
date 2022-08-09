from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

run_machine = True
while run_machine:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        run_machine = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_input):
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)


