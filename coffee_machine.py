import os
from menu import menu  # Importing the menu dictionary
from art import logo

# Initial resources
water = 300
milk = 200
coffee = 100
money = 0

# Flag for handling numeric input errors
number_error_handler = True


# Function to calculate the amount of money inserted by the user
def calculate_money():
    global number_error_handler
    number_error_handler = True
    while number_error_handler:
        print("Please insert coins!")
        quarter = input("How many Quarters?: ")
        dime = input("How many dime?: ")
        nickle = input("How many nickle?: ")
        pennie = input("How many pennie?: ")
        # Checking if all inputs are numeric
        if quarter.isnumeric() and dime.isnumeric() and nickle.isnumeric() and pennie.isnumeric():
            number_error_handler = False
            # Calculating total amount inserted
            pay = 0.25 * int(quarter) + 0.10 * int(dime) + 0.05 * int(nickle) + 0.01 * int(pennie)
            return pay
        else:
            os.system('cls')
            print("Insert numbers only!")


# Main loop of the coffee machine
while True:
    print(logo)
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order in menu:
        for item in menu:
            if order == item:
                # Checking if resources are sufficient for the order
                if water >= menu[item]["Water"] and coffee >= menu[item]["Coffee"]:
                    water -= menu[item]["Water"]
                    coffee -= menu[item]["Coffee"]
                    # Handling payment
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
                                print(f"Here is ${change} in change. \nHere is your {order} ☕️. Enjoy!")
                                input("Tap any key to order!")
                                os.system('cls')
                        else:
                            print("Please pay enough amount for the product!")

    # Reporting resources and money earned
    elif order == "report":
        os.system('cls')
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    # Turning off the machine
    elif order == "off":
        os.system('cls')
        print("Machine in maintenance mode!")
        break  # Exit the loop

    else:
        os.system('cls')
        print("Please input a valid option!")

# Program ends here
input("Tap Enter to Exit!")

