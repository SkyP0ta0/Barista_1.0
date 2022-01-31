from coffe_data import *

# menu variables with ingredients
menu = MENU

# resources/ingredients
# water = resources["water"]
# milk = resources["milk"]
# coffee = resources["coffee"]
n_resources = resources


# Returns True if resources are > than the requirements to make beverage and uses resources
def inventory_check(coffee_choice):
    price = coffee_choice['cost']
    water_required = int(coffee_choice['ingredients']['water'])
    coffee_required = int(coffee_choice['ingredients']['coffee'])
    if not coffee_choice['internalName'] == "espresso":  # creating exception to espresso, since it don't require 'milk'.
        milk_required = int(coffee_choice['ingredients']['milk'])

    if water_required < int(n_resources['water']):
        # updates resources
        n_resources['water'] = int(n_resources['water']) - water_required
        if coffee_required < int(n_resources['coffee']):
            n_resources['coffee'] = int(n_resources['coffee']) - coffee_required
            if price == 1.5:
                return True
            elif milk_required < int(n_resources['milk']):
                n_resources['milk'] = int(n_resources['milk']) - milk_required
                return True  # Returns True if ingredients are available
            else:
                return "Sorry theres not enough milk."
        else:
            return "Sorry theres not enough coffee."
    else:
        return "Sorry theres not enough water."


# returns string with updated reports
def report():
    print(f"Water: {n_resources['water']}ml")
    print(f"milk: {n_resources['milk']}ml")
    print(f"coffee: {n_resources['coffee']}oz")
    print(f"money: ${n_resources['money']}")


# coin calculator. Determines if theres enough money, returns change. prints results.
def coin_calculator(coffee_price):
    print("Please insert coins.")
    total = 0
    for coins in change:
        amount_of_coins = float(input(f"How many {coins}?: "))
        if amount_of_coins == 1:
            total += change[coins]
        else:
            total += change[coins] * amount_of_coins

    if total >= coffee_price:

        cambio = round(total - coffee_price, 2)
        print(f"Here is ${cambio} in change.")
        print("Here is your espresso ☕. Enjoy!")
        n_resources['money'] += coffee_price

    else:
        print("Sorry that's not enough money. Money Refunded")


on = True
while on:
    order = input("what would you like? (Espresso/Latte/Cappuccino): ").lower()

    if order in menu:
        drink = menu[order]
        # function to calculate
        available = inventory_check(drink)
        if available == True:  # if enough inventory, continue
            coin_calculator(drink['cost'])  # checks cost of coffee against money inserted
        else:
            print(available)  # Prints reason to why the drink couldn't be served
    else:
        if order == 'report':
            report()
        elif order == 'off':
            on = False
