numeros = list(range(500,99,-3)) #Aqui haremos una lista con un rango entre 500 a 99 y se incrementa por 3

print("Numeros del 500 al 100 incrementado de 3 en 3")
for num in numeros: #Aqui haremos un bucle donde num sera una variable que pasara por numeros y asi hasta llegar al limite
    print (num)

suma = sum(numeros)
print(suma)

promedio = suma / len(numeros)
print (promedio)

print(f"Suma total: {suma}")
print(f"Promedio total: {promedio:.2f}")