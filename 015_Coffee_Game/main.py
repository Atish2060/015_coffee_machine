from menu import MENU
from menu import resources
profit = 0
on = True


def check_money(ret):
    """
    Checks Balance is sufficient or not
    """
    if ret > 0:
        print(f"Your change is: ${round(ret, 2)}")
    else:
        print("Insufficient Balance!!")


def calc_money():
    """
    Calculates the sum of money
    """
    print("\nPlease insert coins: ")
    quarters = int(input("How many quarters?(1 quarter = $0.25): "))
    dimes = int(input("How many dimes?(1 dime = $0.1): "))
    nickels = int(input("How many nickles?(1 nickle = $0.05): "))
    pennies = int(input("How many pennies?(1 penny = $0.01): "))
    cost = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return cost


def resources_decrease(water, milk, coffee):
    """
    Records the decrease in the resources
    """
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee
    if resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0:
        return False
    else:
        return True


def coffee_machine():
    """
    Main function working as an coffee machine.
    """
    global profit
    print("\nThe options are: \n"
          "-espresso\n"
          "-latte\n"
          "-cappuccino\n"
          "-off(to turn off the machine)\n"
          "-report(to find out the remaining ingredients.)\n")
    option = input("What would you choose? ").lower()

    if option == "espresso":
        print(f"\nThe cost of espresso is: ${MENU["espresso"]["cost"]}")
        if resources_decrease(MENU["espresso"]["ingredients"]["water"], MENU["espresso"]["ingredients"]["milk"],
                              MENU["espresso"]["ingredients"]["coffee"]):
            ret_money = calc_money() - MENU["espresso"]["cost"]
            check_money(ret_money)
            if ret_money > 0:
                profit = profit + MENU["espresso"]["cost"]
        else:
            print("Insufficient ingredients. Please choose another option please !!")
    elif option == "latte":
        print(f"\nThe cost of espresso is: ${MENU["latte"]["cost"]}")
        if resources_decrease(MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["milk"],
                              MENU["latte"]["ingredients"]["coffee"]):
            ret_money = calc_money() - MENU["latte"]["cost"]
            check_money(ret_money)
            if ret_money > 0:
                profit = profit + MENU["latte"]["cost"]
        else:
            print("Insufficient ingredients. Please choose another option please !!")
    elif option == "cappuccino":
        print(f"\nThe cost of espresso is: ${MENU["cappuccino"]["cost"]}")
        if resources_decrease(MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["milk"],
                              MENU["cappuccino"]["ingredients"]["coffee"]):
            ret_money = calc_money() - MENU["cappuccino"]["cost"]
            check_money(ret_money)
            if ret_money > 0:
                profit = profit + MENU["cappuccino"]["cost"]
        else:
            print("Insufficient ingredients. Please choose another option please !!")
    elif option == "report":
        print("The remaining ingredients are: ")
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Profit: ${profit}")
    elif option == "off":
        global on
        on = False
    elif option != "espresso" and option != "latte" and option != "cappuccino" and option != "report" and option != "off":
        print("Choose the correct option please !!")


while on:
    coffee_machine()
