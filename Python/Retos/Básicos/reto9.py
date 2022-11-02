#Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
year=int(input("Introduce un año: "))
if (year % 4== 0 and year % 100 !=0) or year % 400 == 0:
    print("El año", year,"es bisiesto")
else:
    print("El año",year,"no es bisiesto")