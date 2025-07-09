#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 7
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


numero = int(input("Ingrese un numero entero para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para numeros negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")