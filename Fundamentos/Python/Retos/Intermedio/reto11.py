#Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
#NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
#El programa debe mostrar las siguientes opciones para que escoja el usuario:
#(1) Añadir un cliente
#(2) Eliminar cliente por NIF
#(3) Mostrar Cliente por NIF
#(4) Listar TODOS los clientes
#(5) Mostrar ÚNICAMENTE los clientes preferentes
#(6) Finalizar Programa

#Primero creamos la lista de clientes vacía
customers = []

#A continuación, se definen las opciones que podemos realizar:

def options():
  print("¡Hola! ¿Qué acción desea ejecutar?: 1. Añadir un nuevo cliente, 2. Eliminar cliente por NIF, 3. Mostrar cliente por NIF, 4. Mostrar todos los clientes, 5. Mostrar clientes preferentes, 6. Finalizar")

  select = int(input("Seleccione la acción que desea ejecutar: "))
  while select:
    if select == 1:
      addCustomer()
            
    elif select == 2:
      deleteCustomer()
            
    elif select == 3:
      showNifCustomer()
            
    elif select == 4:
      showCustomer()
            
    elif select == 5:
      showVip()
        
    elif select == 6:
      print("Ha finalizado el programa correctamente.")
      exit()
        
    else:
      select = int(input("Debe elegir un número entre el 1 y el 6: "))

#A continuación definimos la función de addCustomer
def addCustomer():
  NIF = str(input("Introduzca el NIF del cliente: "))
  Nombre = str(input("Introduzca el nombre del cliente: "))
  Telf = str(input("Introduzca el teléfono del cliente: "))
  Correo = str(input("Introduzca el correo del cliente: "))
  Preferente = str(input("Indique si el cliente es preferente: sí/no: "))

  if Preferente =="sí":
    Preferente = True
  elif Preferente == "no":
    Preferente = False

  customer = {"NIF" : NIF,
            "Nombre" : Nombre,
            "Telf" : Telf,
            "Correo" : Correo,
            "Preferente" : Preferente}

  customers.append(customer)
  options()

#A continuación, creamos la función para eliminar al cliente por NIF

def deleteCustomer():
  NIF = input('Introduzca el NIF del cliente que desea eliminar: ')
  for i in customers:
    if i["NIF"]==NIF:
      customers.remove(i)
      print("El cliente ha sido eliminado correctamente.")
    else:
      print('No hay clientes relacionados con ese NIF.')
  options()

#A continuación, creamos la función para mostrar clientes según  NIF
def showNifCustomer():
  NIF = input('Introduzca el NIF del cliente: ')
  for i in customers:
    if i["NIF"]==NIF:
      print(f'NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telf: {i["Telf"]}, Correo: {i["Correo"]}, Preferente: {i["Preferente"]}')
    else:
      print('No hay clientes relacionados con ese NIF.')
  options()
  
#A continuación, creamos la función para mostrar todos los clientes
def showCustomer():
  for idx, i in enumerate(customers):
    print(f'NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telf: {i["Telf"]}, Correo: {i["Correo"]}, Preferente: {i["Preferente"]}')
  options()

#A continuación, creamos la función para mostrar los clientes preferentes
def showVip():
  for i in customers:
    if i["Preferente"] == True:
      print(f'NIF: {["NIF"]}, Nombre: {["Nombre"]}, Telf: {["Telf"]}, Correo: {["Correo"]}, Preferente: {i["Preferente"]}')
    else:
      print("No se han encontrado clientes preferentes.")
  options()

options()
