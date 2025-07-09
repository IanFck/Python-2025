import json #Manipulacion archivos Json
import os #Metodos para trabajar con el sistema operativo

ruta = os.path.join("json", "datos.json") #Ruta relativa /json/datos.json

#Leer el archivo Json

with open(ruta, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("\nTodos los usuarios:")
for usuario in datos:
    print(f"ID: {usuario["id"]}, Nombre: {usuario["nombre"]}, Edad:{usuario["edad"]}")

nuevo_usuario = {
    "id":5,
    "nombre": "Fernanda",
    "Edad": 30
}

datos.append(nuevo_usuario)

#with open(ruta, "r", encoding="utf-8") as archivo: