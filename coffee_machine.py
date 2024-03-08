import os
from menu import menu
from art import logo

# resources
water = 300
milk = 200
coffee = 100
money = 0

completed = True
number_error_handler = True


def calculate_money():
    global number_error_handler
    while number_error_handler:

        print("Please insert coins!")
        quarter = input("How many Quarters?: ")
        dime = input("How many dime?: ")
        nickle = input("How many nickle?: ")
        pennie = input("How many pennie?: ")

        if quarter.isnumeric() and dime.isnumeric() and nickle.isnumeric() and pennie.isnumeric():
            number_error_handler = False
            pay = 0.25 * int(quarter) + 0.10 * int(dime) + 0.05 * int(nickle) + 0.01 * int(pennie)
            return pay
        else:
            os.system('cls')
            print("Insert numbers only!")


while completed:
    print(logo)
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order in menu:
        for item in menu:
            if order == item:

                if water >= menu[item]["Water"] and coffee >= menu[item]["Coffee"]:
                    water -= menu[item]["Water"]
                    coffee -= menu[item]["Coffee"]
                    loop = True
                    while loop:
                        payment = calculate_money()
                        if payment >= menu[item]["price"]:
                            change = round(payment - menu[item]["price"], 2)
                            loop = False
                            money += menu[item]["price"]
                            if change == 0:
                                os.system('cls')
                                print(f"Here is your {order} ☕️. Enjoy!")
                            else:
                                os.system('cls')
                                print(f"Here is ${change} in change. \nHere is your {order} ☕️. Enjoy!")
                        else:

                            print("Please pay enough amount for the product!")

    elif order == "report":
        os.system('cls')
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"coffee: {coffee}g")
        print(f"Money: ${money}")
    elif order == "off":
        completed = False
        os.system('cls')
        print("Machine in maintenance mode!")
    else:
        os.system('cls')
        print("Please input a valid input!")

input("Tap Enter to Exit!")
