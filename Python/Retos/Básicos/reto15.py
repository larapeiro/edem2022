#Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def reto15(*sample):
    list= []
    for i in sample:
        list.append(i**2)
    return list

print(reto15(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))