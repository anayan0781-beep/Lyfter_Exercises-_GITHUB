def get_name():
    try:
        name = input("Enter your name: ")

        if name.isdigit():
            raise ValueError("Name cannot be numeric.")

        return name

    except ValueError:
        print("Error: Please enter a valid name.")
        return get_name()


def get_age():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")

        return age

    except ValueError:
        print("Error: Please enter a valid age.")
        return get_age()


def show_message(name, age):
    print(f"Hello {name}, your age is {age}")


def main():
    name = get_name()
    age = get_age()
    show_message(name, age)


if __name__ == "__main__":
    main()