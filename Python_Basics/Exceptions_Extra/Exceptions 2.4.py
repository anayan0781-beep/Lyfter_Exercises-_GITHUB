def sum_values(items):
    total = 0

    for item in items:
        try:
            value = float(item)
            total += value

        except ValueError:
            print(f"Invalid element: {item}")

    print("Total:", total)


def main():
    items = ["10", 5, "3.5", "hello", 20, "Python"]

    sum_values(items)


if __name__ == "__main__":
    main()