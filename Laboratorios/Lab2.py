# Ejercicio 1
print("Ingreso de Productos")
#1. Pedir por consola los precios unitarios (float) y las cantidades (int) de cuatro productos:
precio_martillo = float(input("Precio unitario del Martillo: $"))
cantidad_martillo = int(input("Cantidad de Martillos: "))

precio_clavos = float(input("Precio unitario de los Clavos: $"))
cantidad_clavos = int(input("Cantidad de Clavos: "))

precio_serrucho = float(input("Precio unitario del Serrucho: $"))
cantidad_serrucho = int(input("Cantidad de Serruchos: "))

precio_tornillos = float(input("Precio unitario de los Tornillos: $"))
cantidad_tornillos = int(input("Cantidad de Tornillos: "))

#2.- Calcular y mostrar los subtotales para cada producto y redondearlos a 2 decimales.
subtotal_martillo = round(precio_martillo * cantidad_martillo, 2)
subtotal_clavos = round(precio_clavos * cantidad_clavos, 2)
subtotal_serrucho = round(precio_serrucho * cantidad_serrucho, 2)
subtotal_tornillos = round(precio_tornillos * cantidad_tornillos, 2)

# Mostrar subtotales
print("\n=== Subtotales ===")
print(f"Subtotal Martillo: ${subtotal_martillo}")
print(f"Subtotal Clavos: ${subtotal_clavos}")
print(f"Subtotal Serrucho: ${subtotal_serrucho}")
print(f"Subtotal Tornillos: ${subtotal_tornillos}")

# Calcular suma total, máximo, mínimo, promedio de precios y el IVA
suma_total = round(subtotal_martillo + subtotal_clavos + subtotal_serrucho + subtotal_tornillos, 2)
valor_max = max(subtotal_martillo, subtotal_clavos, subtotal_serrucho, subtotal_tornillos)
valor_min = min(subtotal_martillo, subtotal_clavos, subtotal_serrucho, subtotal_tornillos)
promedio_precios = round((precio_martillo + precio_clavos + precio_serrucho + precio_tornillos) / 4, 2)
iva = round(suma_total * 0.19, 2)

#3.- Imprimir los siguientes resultados, en este orden:
print("\n=== Resultados Finales ===")
print(f"Suma total de los subtotales: ${suma_total}")
print(f"Valor máximo entre los subtotales: ${valor_max}")
print(f"Valor mínimo entre los subtotales: ${valor_min}")
print(f"Promedio del precio unitario de las herramientas: ${promedio_precios}")
print(f"IVA (19%) del total: ${iva}")

#Ejercicio 2
#1.- Ingresar por terminal un resumen en formato string.

resumen = input("Ingrese el resumen (abstract) del paper científico:\n")

#2. Crear una variable booleana, que permita imprimir True o False para indicar si el resumen ingresado cumple con un límite de 50 caracteres.

cumple_limite = len(resumen) = 50
print(f"\n¿El resumen tiene 50 caracteres o menos?: {cumple_limite}")

# 3. Mostrar la siguiente información, separados por saltos de línea:
print("\n=== Análisis del Resumen ===")
print(f"a) Longitud total del resumen: {len(resumen)}")
print(f"b) Resumen en mayúsculas: {resumen.upper()}")
print(f"c) Resumen en minúsculas: {resumen.lower()}")
print(f"d) Número de veces que aparece la vocal 'e': {resumen.lower().count('e')}")
print(f"e) Primeros 15 caracteres: {resumen[:15]}")
print(f"   Últimos 15 caracteres: {resumen[-15:]}")
print(f"f) Palabras unidas por comas: {','.join(resumen.split())}")
