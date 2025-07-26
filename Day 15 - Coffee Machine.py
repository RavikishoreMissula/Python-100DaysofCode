menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
    'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
    'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
    'cost': 3.0,
    },
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

coffee_image = '☕'

def calculate_total():
    """Calculates the total of the coins given by the user. Returns Total money."""
    quarters = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = round(quarters * 0.25 + dime * 0.10 + nickels * 0.05 + pennies * 0.01, 2)
    return total_money

def check_resources(menu_items, resources_available, user_choice):
    """checks if the resources are available to fulfil the user choice. Returns True or False."""
    for ingredient_item in menu_items[user_choice]['ingredients']:
        if resources_available[ingredient_item] < menu_items[user_choice]['ingredients'][ingredient_item]:
            print(f"Sorry there is not enough {ingredient_item}")
            return False
    return True

# todo 1: when user enter report then print report of available resources
money = 0
machine_running = True

while machine_running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['cost']}g")
        print(f"Money: ${money}")
    elif user_input == 'off':
        machine_running = False
    elif user_input in menu:
        if check_resources(menu, resources, user_input):
            total_money_input = calculate_total()
            if total_money_input < menu[user_input]['cost']:
                print("Sorry there is no enough money. Money refunded.")
            elif total_money_input > menu[user_input]['cost']:
                balance = round(total_money_input - menu[user_input]['cost'], 2)
                money += menu[user_input]['cost']
                for ingredient in menu[user_input]['ingredients']:
                    resources[ingredient] -= menu[user_input]['ingredients'][ingredient]
                print(f"Here is ${balance} in change.")
                print(f"Here is your {user_input} {coffee_image}. Enjoy!")
    else:
        print("Invalid Option. Please try again.")