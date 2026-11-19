name = input("Ingrese su nombre: ")

if name.isdigit():
    raise ValueError("El nombre no puede ser un número")

try:
    age = int(input("Ingrese su edad: "))
except ValueError:
    print("Número no valido")