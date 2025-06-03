nombre = "Ian Andres"
edad = 22 
estudiante = True 

print (type(nombre))
print (type(edad))
print (type(estudiante))

pi = 3.1416
gravedad = 9.8
VELOCIDAD_LUZ = 2997292458

print ("Valor de signo Pi:", pi)
print ("Valor de la gravedad:", gravedad, "m/s²")
print ("Valor de la velocidad de la luz:", VELOCIDAD_LUZ, "m/s²") 

Año = input("Ingresa un año de nacimiento")
nacimiento = int(Año)
edad = 2025 - nacimiento
print ("Tienes", edad, "Años")

nombre_completo = input("Dame tu nombre completo")
año_de_nacimiento = int(input("Dame tu año de nacimiento"))
edad = 2025 - año_de_nacimiento
es_mayor = edad >= 18 

print ("Tu nombre completo es:", nombre_completo, "tu año de nacimiento es:", año_de_nacimiento, "tu edad es:", edad, "Y eres mayor de edad (Si sale true es porque si, si sale False no)", es_mayor)

nombre_del_producto = input("Dame el nombre de tu producto")
precio_unitario = float(input("Dame el precio de tu producto"))
cantidad = int(input("Dime la cantidad que quieres comprar"))
total_sin_descuento = precio_unitario * cantidad

if total_sin_descuento > 100000:
    descuento = total_sin_descuento * 0.1
else:
    descuento = 0

precio_final = total_sin_descuento - descuento

print ("Este es tu producto:", nombre_del_producto)
print ("Esta es la cantidad de tus productos:", cantidad)
print ("Total sin descuento", total_sin_descuento)
print ("Descuento aplicado:", descuento)
print ("Total a pagar:", precio_final)