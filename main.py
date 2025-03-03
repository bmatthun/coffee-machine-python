from traceback import print_tb

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

machine_money = 0.00

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def ask_user_input():
    user_input = input("What would you like? Type espresso, latte or cappuccino: ")
    if user_input.lower() == 'espresso' or user_input ==  'latte' or user_input == 'cappuccino':
        return user_input
    # Prompting off the coffee machine stops working.
    elif user_input.lower() == "off":
        exit()
    elif user_input.lower() == "report":
        # Print out the report
        print_report(resources, machine_money)
    else:
        print("Wrong user input!")
        return ask_user_input()

# Printing the report about available resources and money in the machine
def print_report(resources, money):
    print(f"Milk: {resources['milk']}ml")
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# Check availability of resources
def check_resources(user_choice, resources):
    chosen_coffee_product = MENU[user_choice]
    for ingredient in MENU[user_choice]["ingredients"]:
        # If there is not enough ingredient for making the chosen product
        if MENU[user_choice]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}. Try another product.")
            return False
        # If enough ingredient for making the chosen product
        else:
            return True

def check_money(user_input):
    print("Please insert coins: \n")
    global machine_money
    coins = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickle": 0.05,
        "penny": 0.01
    }
    user_money = 0.00
    for key in coins:
        money_amount = (input(f"{key}: "))
        user_money += int(money_amount) * coins[key]

    if user_money < MENU[user_input]["cost"]:
        print("Not enough money for the purchase. Money refunded.")
        return False
    elif user_money > MENU[user_input]["cost"]:
        user_money -= MENU[user_input]["cost"]
        print(f"Here is ${user_money - MENU[user_input]["cost"]} dollars in change")
        machine_money += MENU[user_input]["cost"]
        return True
    else:
        machine_money += MENU[user_input]["cost"]
        return True

def operate():
    while True:
    # Return value can be the name of the product or no return value at all
        user_input = ask_user_input()
        selected_product = MENU[user_input]
        has_resources = check_resources(user_input, resources)
        if not has_resources:
            continue
        has_user_money = check_money(user_input)
        if not has_user_money:
            continue
        else:
            for ingredient in selected_product["ingredients"]:
                resources[ingredient] -= selected_product["ingredients"][ingredient]
            print(f"Here is your {user_input}. Enjoy it! ☕")

operate()
