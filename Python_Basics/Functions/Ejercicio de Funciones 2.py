def show_name():
    name = "Ana"
    print(name)


show_name()

#print(name)

#La variable name es una variable local, porque fue creada dentro de show_name().
#NameError: name 'name' is not defined
#una variable creada dentro de una función normalmente solo existe dentro de esa función.

#Si quiero usar la variable fuera de la función
#Las variables creadas dentro de una función tienen un local scope y no pueden ser utilizadas directamente desde afuera

name = "Ana"

def show_name():
    print(name)


show_name()
print(name)


