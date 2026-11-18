my_list = [122, 203, 300, 412, 560, 611, 781, 830, 910]

even_numbers = []

for number in my_list:
    if number % 2 == 0:
        even_numbers.append(number)

print("Original list:", my_list)
print("List without odd numbers:", even_numbers)