def count_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    words = content.split()
    return len(words)


def main():
    filename = input("Enter the filename: ")
    total_words = count_words(filename)

    print(f"This file contains {total_words} words.")


if __name__ == "__main__":
    main()
    