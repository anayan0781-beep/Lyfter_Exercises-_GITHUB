name = input("Enter your name: ")

if name.isdigit():
    raise ValueError("El nombre no puede ser un número")

print("Hello,", name)




