name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age <= 2:
    life_stage = "baby"
elif age <= 9:
    life_stage = "child"
elif age <= 12:
    life_stage = "preteen"
elif age <= 17:
    life_stage = "teenager"
elif age <= 25:
    life_stage = "young adult"
elif age <= 59:
    life_stage = "adult"
else:
    life_stage = "older adult"

print("First name:", name)
print("Last name:", last_name)
print("Age:", age)
print("Life stage:", life_stage)