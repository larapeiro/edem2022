#Escribe un programa que pueda decirte si un número (número entero) es primo o no
def primo(num):
    if num <1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


num = int(input("Introduce un número: "))
result=primo(num)

if result is True:
    print("El número es primo")
else:
    print("El número no es primo")

