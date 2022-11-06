#Escribe un programa que sea capaz de pedirle a un usuario por consola que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola. Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego terminar.
password:str = input('Introduce una contraseña: ')
password_correcta = "admin"
while (password!=password_correcta):
    password = input("Contraseña incorrecta. Vuelva a intentarlo: ")
if (password == password_correcta):
    print("Bienvenido al programa señor ADMIN")