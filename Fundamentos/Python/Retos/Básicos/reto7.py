#Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
password:str = input('Introduce una contraseña: ')
password_correcta = "edem2022"
if (password.lower()==password_correcta.lower()):
    print("La contraseña introducida coincide.")
else:
    print("La contraseña no coincide.")