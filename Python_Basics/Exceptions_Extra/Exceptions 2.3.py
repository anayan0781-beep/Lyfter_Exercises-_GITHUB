def convertir_a_entero(lista):
    for valor in lista:
        try:
            numero = int(valor)
            print(valor, "convertido a", numero)
            print(numero, "convertido correctamente")

        except ValueError:
            print("No se pudo convertir el elemento:", valor)


my_list = ['7', 'hola', '15', '8.2']

print("Resultado:")
convertir_a_entero(my_list)