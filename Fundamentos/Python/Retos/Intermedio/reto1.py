#Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.
#Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final de la compra.

import datetime

#Primero creamos los diccionarios para cada disco
Zigarros = {'title':'Zigarros', 'artist':'Loz Zigarros', 'year':2016, 'price': 15, 'genre':'Rock'}
Discomania = {'title':'Discomania', 'artist':'Dorian', 'year':2000, 'price':20, 'genre':'Electro'}
Tormentas = {'title':'Tormentas', 'artist':'Mandangas', 'year':2022, 'price':10, 'genre':'Pop'}
Car = {'title':'The Car', 'artist':'Arctic', 'year':2022, 'price':25, 'genre':'Rock'}
Reptilia = {'title':'Reptilia', 'artist':'Strokes', 'year':2012, 'price':10, 'genre':'Metal'}
Eterna = {'title':'Eterna', 'artist':'Funambulista', 'year':2008, 'price':20, 'genre':'Death Metal'}
Noche = {'title':'Noche', 'artist':'LOL', 'year':2014, 'price':25, 'genre':'Black Metal'}

#A continuación, creamos una lista que contiene la información de todos los discos agrupada
discosTienda = [Zigarros, Discomania, Tormentas, Car, Reptilia, Eterna, Noche]

def reto1d():
  numero = 1
  compra = [] 

  #Bucle que muestra los discos disponibles para comprar
  print("¡Hola! Estos son los discos disponibles:")
  for idx, disco in enumerate(discosTienda):
    print(f'Disco nº {idx+1}: Album: {disco["title"]},  Artista: {disco["artist"]},  Precio: {disco["price"]} €,  Género: {disco["genre"]}')


  #Bucle que permite al usuario elegir que discos quiere comprar, añadirlos o finalizar la compra
  compraDiscos = int(input('Introduce el número del disco que quieres comprar o pulsa 0: '))
  while (compraDiscos != 0):
    compra.append(discosTienda[compraDiscos-1])
    compraDiscos = int(input('Si quieres añadir otro disco introduce su número, o pulsa 0 para finalizar la compra: '))
  
  
  #Creamos el bucle donde se muestran los discos comprados por el usuario
  descuento = 0
  precio = 0
  sinDescuento = 0
  for disco in compra:
    if(disco["genre"] == 'Black Metal' or disco["genre"] == 'Electro'): 
      descuento += disco["price"]*0.3
      precio += disco["price"]-descuento
      sinDescuento += disco["price"]
    else: 
      precio += disco["price"]
      sinDescuento += precio
      
  #Imprimimos la fecha y hora de la compra usando datetime.today
  print(f'La compra fue realizada: {datetime.datetime.today()}')
  #Imprimimos el precio total de la compra
  print(f'El precio de la compra es: {sinDescuento} €')
  if(descuento != 0):
    #Imprimimos el descuento de la compra si el disco seleccionado lo tiene aplicado según su género
    print(f'El descuento total aplicado a su compra: {descuento} €')
    #Imprimimos el precio final con descuento aplicado
    print(f'El precio final de la compra es: {round(precio,2)} €')