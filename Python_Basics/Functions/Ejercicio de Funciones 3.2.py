def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [4, 6, 2, 29]

result = calculate_sum(numbers)

print(result)