inventario = {
        "Manzana":(1200,2000,1500),
        "Platano": (1000,1000,1500),
        "Cereza": (600,1200,1500)
}

precios_platano = inventario["Platano"]
precios_nuevos_platanos = list(set(precios_platano)) #Lo cambiamos a set porque no permite duplicados y luego lo transformamos en una lista para que tenga orden

tipos_frutas = list(inventario.keys()) #Creamos con list para transformar la tupla en una lista porque es lo que nos pidieron y usamos .keys para llevarnos las llaves de el diccionario

promedio_platano = sum(precios_nuevos_platanos) / len(precios_nuevos_platanos) #Para sacar un promedio siempre usamos Len para que nos divida

print(inventario)
print(precios_nuevos_platanos)
print(tipos_frutas)
print("Promedio de precios únicos del plátano:", "$", promedio_platano) 

