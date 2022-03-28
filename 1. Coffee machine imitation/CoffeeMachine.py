from Data import MENU, resources

profit = 0
more_customers = True


def check_resources(order_ingredients):
    for ingredients in order_ingredients:
        if order_ingredients[ingredients] > resources[ingredients]:
            print(f"Sorry there is not enough {ingredients}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = float(input("How many quarters? ")) * 0.25
    total += float(input("How many dimes? ")) * 0.10
    total += float(input("How many nickels? ")) * 0.05
    total += float(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_inserted, product_cost):
    if money_inserted >= product_cost:
        change = round(money_inserted - product_cost, 2)
        print(f"Here's ${change} in change.")
        global profit
        profit += product_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while more_customers:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        more_customers = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choice not in MENU:
            print("You did not select any of the available options. Try again.")
        else:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
