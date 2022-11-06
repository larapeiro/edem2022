#Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad:int = int(input("Introduzca su edad para comprobar si es mayor de edad: "))
if (edad >= 18):
    print("Usted es mayor de edad.")
else:
    print("Usted no es mayor de edad.")