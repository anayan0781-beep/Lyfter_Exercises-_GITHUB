#Este ejercicio se puede hacer usando una función con un parámetro (la lista) y return para devolver la suma

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)

print(result)

#numbers es el parámetro que recibe la función.
#total = 0 comienza la suma en cero.
#El for recorre cada número de la lista.
#total += number va sumando cada elemento.
#return total devuelve el resultado de la suma.