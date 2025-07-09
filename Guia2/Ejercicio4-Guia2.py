#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 4
def cubos_nicomaco(n):
    #primer número impar
    impar_actual = 1  

    for i in range(1, n + 1):
        suma = 0
        secuencia = []
#siguiente número impar
        for j in range(i):
            secuencia.append(impar_actual)
            suma += impar_actual
            impar_actual += 2  

        #resultado en formato "n^3 = ... = resultado"
        secuencia_str = ' + '.join(map(str, secuencia))
        print(f"{i}^3 = {secuencia_str} = {suma}")
try:
    n = int(input("Ingrese la cantidad de cubos que desea mostrar: "))
    if n > 0:
        cubos_nicomaco(n)
    else:
        print("Tiene que ingresar un número entero positivo.")
except ValueError:
    print("Entrada inválida, debe ingresar un número entero.")