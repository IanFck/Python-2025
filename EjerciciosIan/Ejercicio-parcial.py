inventario = {
  "pan": {"cantidad": 20, 
        "precio": 500
        },
  "leche": {"cantidad": 15, 
        "precio": 900
        },
"huevos": {
      "cantidad": 30, 
      "precio": 250}
}

inventario["leche"]["cantidad"] = 10 #Actualizar variables
inventario["pan"]["precio"] = 550
print(inventario)

inventario["mantequilla"] = {"cantidad": 12,"precio": 1200} #Crear nuevas variables
print(inventario)

inventario["cafe"] = {"cantidad": 0, "precio": 800}

for producto in list(inventario.keys()): #Aqui creamos la variable producto que recorrera uan lista con las llaves del diccionario inventario
      if inventario[producto]["cantidad"] == 0: #Aqui si en la variable cantidad de la llave producto es 0
            del inventario[producto] #Se eliminara la variable producto

print(inventario)

for producto in inventario:
      if inventario[producto]["precio"] >= 900:
            print(producto, inventario[producto])

total_cantidad = sum(inventario[producto]["cantidad"] for producto in inventario) #Esta línea recorre todos los productos en el inventario, toma la cantidad de cada uno y suma esas cantidades para obtener el total de unidades disponibles.
print(total_cantidad)


