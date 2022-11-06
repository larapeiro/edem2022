def reto1():
  nombre:str = "Pepe"
  apellidos:str = "Perez"
  edad:int = 20
  email:str = "pepeperez@gmail.com"
  telefono = 123456789
  casado:bool = False
  hijos:bool = False
  amigos:list = ["Alex", "Bea", "Carlos", "Dani"]
  peliculas:dict = { 
    "titulo1": "Titanic",
    "titulo2": "El Pregón",
    "titulo3": "Los Intocables"
  }
  
      
  print(f"""Los datos del contacto son
Nombre: {nombre}
Apellido: {apellidos}
Edad: {edad}
Email: {email}
Tlf: {telefono}
¿Casado?: {casado}
¿Hijos?: {hijos}
Lista amigos: {amigos}
Películas: {peliculas}""")

print(reto1())