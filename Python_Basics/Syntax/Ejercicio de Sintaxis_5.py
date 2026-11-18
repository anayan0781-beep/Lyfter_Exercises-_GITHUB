number_of_grades = int(input("Enter the number of grades: "))

approved_count = 0
failed_count = 0

approved_sum = 0
failed_sum = 0
total_sum = 0

for i in range(number_of_grades):
    grade = float(input(f"Enter grade {i + 1}: "))

    total_sum += grade

    if grade > 70:
        approved_count += 1
        approved_sum += grade
    elif grade < 70:
        failed_count += 1
        failed_sum += grade

average = total_sum / number_of_grades

if approved_count > 0:
    approved_average = approved_sum / approved_count
else:
    approved_average = 0

if failed_count > 0:
    failed_average = failed_sum / failed_count
else:
    failed_average = 0

print("\n--- Results ---")
print("Approved grades:", approved_count)
print("Failed grades:", failed_count)
print("Average of all grades:", average)
print("Average of approved grades:", approved_average)
print("Average of failed grades:", failed_average)

