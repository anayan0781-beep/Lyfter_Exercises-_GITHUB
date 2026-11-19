def show_menu(current_number):
    print("\nCurrent number:", current_number)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def perform_operation(current_number, option):

    if option == "1":
        try:
            number = float(input("Enter a number to add: "))
            current_number += number
        except ValueError:
            print("Error: Invalid number.")

    elif option == "2":
        try:
            number = float(input("Enter a number to subtract: "))
            current_number -= number
        except ValueError:
            print("Error: Invalid number.")

    elif option == "3":
        try:
            number = float(input("Enter a number to multiply: "))
            current_number *= number
        except ValueError:
            print("Error: Invalid number.")

    elif option == "4":
        try:
            number = float(input("Enter a number to divide by: "))

            if number == 0:
                print("Error: You cannot divide by zero.")
            else:
                current_number /= number

        except ValueError:
            print("Error: Invalid number.")

    elif option == "5":
        current_number = 0
        print("Result cleared.")

    return current_number


def main():
    current_number = float(input("Enter the initial number: "))

    while True:
        show_menu(current_number)

        option = input("Select an option: ")

        if option == "6":
            print("Calculator closed.")
            break

        elif option in ["1", "2", "3", "4", "5"]:
            current_number = perform_operation(current_number, option)

        else:
            print("Error: Invalid option.")


if __name__ == "__main__":
    main()