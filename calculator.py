# function to print a welcom message
def print_welcome_message():
    print("*******************************************")
    print("\t Welcome to the mini-calculator")
    print("*******************************************\n")


# funtion to ask the user to enter two numbers with error handling
def input_two_number():
    while True:
        try:
            num1 = float(input("Enter the fisrt number : "))
            num2 = float(input("Enter the second number : "))
            break
        except ValueError:
            print("Error: please enter valid numbers")

    return num1, num2


# function to print the menu and get the user's choice
def print_menu_and_get_choice():
    print("***************** MENU ******************** ")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    user_choice = input("Enter your choice (1-5) : ")

    while user_choice not in ["1", "2", "3", "4", "5"]:
        user_choice = input("Invalid choice. Enter your choice (1-5) : ")

    return user_choice


# function to perform mathematical operations
def sum(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero")


# function to handle user choice
def handle_user_choice(choice):
    match choice:
        case '1':
            num1, num2 = input_two_number()
            result = sum(num1, num2)
            print(f"the sum of {num1} + {num2} is equal to {result}\n")
        case '2':
            num1, num2 = input_two_number()
            result = substraction(num1, num2)
            print(f"the substraction of {num1} + {num2} is equal to {result}")
        case '3':
            num1, num2 = input_two_number()
            result = multiplication(num1, num2)
            print(f"the multiplication of {num1} + {num2} is equal to {result}")
        case '4':
            num1, num2 = input_two_number()
            result = division(num1, num2)
            print(f"the division of {num1} + {num2} is equal to {result}")

        case '5':
            print("thank you for using program !!!")
            return True
        case _:
            print("Invalid choice")

    return False


# main entry point of the program
if __name__ == '__main__':
    print_welcome_message()
    while True:
        user_choice = print_menu_and_get_choice()
        if handle_user_choice(user_choice):
            break
        # print menu again after each operation
        print_menu_and_get_choice()