numbers = []

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

highest_number = max(numbers)

print("Numbers entered:", numbers)
print("The highest number was:", highest_number)
