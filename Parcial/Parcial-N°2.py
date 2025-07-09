# Para llamar claves[][] #pop #append
#Parcial 2 Ian Fack

#A Crear un diccionario cuyas claves sean los números de ingreso y cuyos valores sean sub-diccionarios con las claves: "Nombre", "Peso", "Edad" y "Tamaño". Luego imprimir eldiccionario
veterinario = {
            101: {"Nombre": "Luna", "Peso": 1.2, "Edad": 3, "Tamaño":30},
            102: {"Nombre": "Michi","Peso": 0.8, "Edad": 2, "Tamaño": 25},
            103: {"Nombre": "Pepito", "Peso": 2.5, "Edad": 5, "Tamaño": 35}
}

print(veterinario)
#B Recorrer el diccionario principal con un bucle y, en cada sub-diccionario, añadir la clave "Clasificación-Peso"

for datos in veterinario.values():
    peso = datos["Peso"]
    if peso < 1:
        datos["Clasificacion-Peso"] = "Bajo Peso"
    elif 1 <= peso <= 4:
        datos["Clasificacion-Peso"] = "Normal"
    else:
        datos["Clasificacion-Peso"] = "Sobre Peso"



#C Crear otro bucle para agregar la clave "Categoría-Etaria" basada en la edad:
for datos in veterinario.values():
    try:
        edad = datos["Edad"]
        if edad < 4:
            datos["Categoria-Etaria"] = "Cachorro"
        elif edad <= 12:
            datos["Categoria-Etaria"] = "Joven"
        else:
            datos["Categoria-Etaria"] = "Adulto"
    except:
        datos["Categoria-Etaria"] = "Desconocida"


#D Crear una lista de tuplas, donde el primer elemento de la tupla es el “N° de Ingreso”, y elsegundo valor es el “Peso”. Luego, ordenarla de menor a mayor peso

lista_pesos = [(clave, datos["Peso"]) for clave, datos in veterinario.items()]
lista_pesos.sort(key=lambda x: x[1])
print(lista_pesos)


#E Implementar un bucle que pida al usuario datos de nuevos gatitos, con todos los datos de la tabla: “N° de Ingreso”, “Nombre”, “Peso”, “Edad”, y “Tamaño”. Después de cada ingreso, preguntar “¿Desea agregar otro gatito? (s/n)”
while True:
    try:
        num = int(input("Número de ingreso: "))
        nombre = input("Nombre: ")
        peso = float(input("Peso (kg): "))
        edad = int(input("Edad (meses): "))
        tamaño = int(input("Tamaño (cm): "))
        veterinario[num] = {
            "Nombre": nombre,
            "Peso": peso,
            "Edad": edad,
            "Tamaño": tamaño
        }
    except:
        print("Dato inválido. Intenta de nuevo.")
    if input("¿Deseas agregar otro gatito? (s/n): ").lower() != 's':
        break



#F Pedir al usuario el número de ingreso de un gatito existente y el nuevo tamaño:
num = int(input("Número de ingreso del gatito: "))
if num in veterinario:
    nuevo_tamaño = int(input("Nuevo tamaño en cm: "))
    veterinario[num]["Tamaño"] = nuevo_tamaño
else:
    print("No se encontró el número de ingreso.")


#G Crear una lista con todos los valores de "Peso", y luego calcular e imprimir

pesos = [datos["Peso"] for datos in veterinario.values()]
promedio = sum(pesos) / len(pesos)
min_peso = min(pesos)
max_peso = max(pesos)
min_ingreso = min(veterinario.items(), key=lambda x: x[1]["Peso"])[0]



