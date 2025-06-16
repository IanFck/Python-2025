#Ejercicio 1
productos = ["Smartphone", "Laptop", "Tablet", "Smartwatch"]
valores = [300, 800, 150, 200]
stock = {
    "Smartphone":25,
    "Laptop": 12,
    "Tablet": 8,
    "Smartwatch": 4
}

#Min y max
max_precio = max(valores)
min_precio = min(valores)

#Nombre del producto mas caro y mas barato
prod_max = productos[valores.index(max_precio)]
prod_min = productos[valores.index(min_precio)]

print(f"El articulo mas caro es {prod_max} con un valor de {max_precio}")
print(f"El articulo mas barato es {prod_min} con un valor de {min_precio}")
#Categoria
for prod, precio in zip(productos, valores):
    if precio <= 200:
        Categoria = "Producto economico"
    elif precio >=200 and precio <= 500:
        Categoria = "Producto estandar"
    else:
        Categoria = "Producto premium"
    print(f"{prod}: ${precio} --> {Categoria}")
print()

for prod, Cantidad in stock.items():
    if Cantidad < 10:
        print (f"{prod}: {Cantidad} unidades")