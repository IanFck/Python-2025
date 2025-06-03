#Ejercicio 4 

print ("Hola te calculare un programa de gestion de inventario")
producto = input("Ingresa el nombre de tu producto")
precio = float(input("Ingresa tu valor unitario"))
stock = int(input("Ingresa la cantidad de stock del producto"))

valor_total = precio * stock 
if valor_total > 100000:
    Umbral = True
else:
    Umbral = False

print ("El nombre de tu producto es: ", producto)
print ("La cantidad de stock: ", stock) 
print ("Y el estado de tu umbral es (Si es True es mayor a 100.000 y si es inferior es False): ", Umbral)
print (round(valor_total , 2))

