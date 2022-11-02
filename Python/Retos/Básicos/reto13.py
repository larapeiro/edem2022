# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math
def area_tri(base, altura):
    area_tri=float(base) * float(altura)/2
    return area_tri

base=input("Introduce la base del triángulo: ")
altura=input("Introduce la altura del triángulo: ")
area=area_tri(base,altura)
print(f"El resultado es: {area}")


def area_circ (radio):
  area_circ = math.pi*(radio**2)
  return area_circ

radio=float(input("Introduce el radio del círculo: "))
area= area_circ(radio)
print(f"El resultado es: {area}")



