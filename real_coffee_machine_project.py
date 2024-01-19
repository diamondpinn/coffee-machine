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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Calculate the monetary value of the coins inserted."""
    cent = 0.01
    penny = 1 * 0.01
    nickel = 5 * 0.01
    dime = 10 * 0.01
    quarter = 25 * 0.01

    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickels = int(input("How many nickels?: "))
    user_pennies = int(input("How many pennies?: "))

    user_quarters_dollars = user_quarters * quarter
    user_dimes_dollars = user_dimes * dime
    user_nickels_dollars = user_nickels * nickel
    user_pennies_dollars = user_pennies * penny

    return float(user_quarters_dollars + user_dimes_dollars + user_nickels_dollars + user_pennies_dollars)

def make_coffee(choice, cost):
    """Deduct resources and handle change for successful transactions."""
    global profit
    if is_resource_sufficient(MENU[choice]["ingredients"]):
        user_payment = process_coins()
        if user_payment >= cost:
            change = round(user_payment - cost, 2)
            profit += cost
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {choice}, ☕ Enjoy!")
            # Deduct resources
            for item in MENU[choice]["ingredients"]:
                resources[item] -= MENU[choice]["ingredients"][item]
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Order cannot be processed due to insufficient resources.")

print("Welcome to Diamond's Coffee Shop")

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino/off/report): ").lower()

    if user_choice == "off":
        print("Coffee machine is turned off.")
        break
    elif user_choice == "report":
        print("Report:")
        for item, quantity in resources.items():
            print(f"{item.capitalize()}: {quantity}")
        print(f"Money: ${profit:.2f}")
    elif user_choice in MENU:
        cost = MENU[user_choice]["cost"]
        make_coffee(user_choice, cost)
    else:
        print("Invalid choice. Please enter a valid option.")
