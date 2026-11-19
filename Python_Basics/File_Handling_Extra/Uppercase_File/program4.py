def add_record(filename):
    text = input("Enter a new record: ")

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")

    print("Record added successfully!")


def main():
    add_record("records.txt")


if __name__ == "__main__":
    main()