#Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
from reto13 import area_circ
from reto13 import radio


def vol_cil(longitud):
    r=area_circ(radio)
    return r*longitud

longitud=float(input("Introduce la longitud del cilindro: "))
resultado=vol_cil(longitud)

print (f"El volumen del cilindro es: {resultado}")

