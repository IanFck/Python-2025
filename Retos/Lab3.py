#Respuestas lab 3 
#1. Según registros del año 2025, se dispone de la siguiente información de tres ciudades  del Archipiélago de Chiloé:
#A) Crear un diccionario que contenga como claves el código postal de cada ciudad. Cada clave debe tener como valor un sub-diccionario con la siguiente información: "Ciudad", "Temperatura" y "Precipitación".
datos_climaticos = {
            5700000: {
                    "Ciudad": "Castro",
                    "Temperatura": 11.8,
                    "Precipitación": 2000},
            5770000: {
                    "Ciudad": "Chonchi",
                    "Temperatura": 8.3,
                    "Precipitación": 2800},
            5790000: {
                    "Ciudad": "Quellón",
                    "Temperatura": 10.2,
                    "Precipitación": 2950}
}
# Luego imprimir el diccionario.
print(datos_climaticos)

#B) Agregar a cada sub-diccionario una nueva clave llamada "Clima" que se determine de acuerdo con la temperatura promedio anual utilizando condicionales:
for datos in datos_climaticos.values():
    temp = datos["Temperatura"]
    if temp >= 15:
        datos["Clima"] = "Templado"
    elif temp >= 10:
        datos["Clima"] = "Frío"
    else:
        datos["Clima"] = "Muy frío"

# Imprimir resultado final
for cod_postal, info in datos_climaticos.items():
    print(f"Código Postal: {cod_postal}, Datos: {info}")

#C) Agregar al sub-diccionario de Castro una nueva clave "Meses Más Lluviosos" que contenga una lista vacía. Luego, utilizar el método correspondiente de Python, para agregar los tres meses uno a uno en cada ciudad. Los meses a agregar son: Mayo, Junio, Julio.
for ciudad in datos_climaticos.values():
    ciudad["Meses Más Lluviosos"] = []

meses = ["Mayo", "Junio", "Julio"]
for ciudad in datos_climaticos.values():
    ciudad["Meses Más Lluviosos"].append("Mayo")
    ciudad["Meses Más Lluviosos"].append("Junio")
    ciudad["Meses Más Lluviosos"].append("Julio")

for ciudad in datos_climaticos.values():
    ciudad["Meses Más Lluviosos"].remove("Junio")

for cod_postal, datos in datos_climaticos.items():
    print(f"Código Postal: {cod_postal} -> {datos}")

datos_climaticos[5770000]["Ciudad"] = "Ciudad de los Tres Pisos"

#D) D) Actualizar el valor de "Ciudad" para la ciudad de Chonchi, cambiándolo por "Ciudad de los Tres Pisos" utilizando el método adecuado de Python.
datos_climaticos[5770000]["Ciudad"] = ["Ciudad de los tres pisos"]



#E) E) Crear una lista llamada “lluvias” que contenga la precipitación de las tres ciudades 
lluvias = [
    datos_climaticos[5700000]["Precipitación"],  # Castro
    datos_climaticos[5770000]["Precipitación"],  # Ancud
    datos_climaticos[5790000]["Precipitación"]   # Quellón
]

suma_total = sum(lluvias)
print(f" Suma total de precipitaciones: {suma_total} mm")
mayor = max(lluvias)
menor = min(lluvias)
print(f" Mayor precipitación: {mayor} ")
print(f" Menor precipitación: {menor} ")

indice_mayor = lluvias.index(mayor)
print(f"Índice de la precipitación más alta: {indice_mayor}")



#F) Imprimir nuevamente el diccionario completo con todos los cambios.

for codigo_postal, datos in datos_climaticos.items():
    print(f"Código Postal: {codigo_postal}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
    print("-" * 40)


#G) Obtener una lista de tuplas con las claves y valores del diccionario utilizando el método correspondiente.
lista_tuplas = list(datos_climaticos.items())
for tupla in lista_tuplas:
    print(tupla)
    


