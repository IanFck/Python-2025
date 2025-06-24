inventario = {
        "Manzana":(1200,2000,1500),
        "Platano": (1000,1000,1500),
        "Cereza": (600,1200,1500)
}

print(inventario)



tipos_frutas = inventario
tipos_frutas.keys
print(tipos_frutas)


precios_platano = (inventario["Platano"])
print(precios_platano)

promedio_platano = (inventario["Platano"],round)
print(promedio_platano)