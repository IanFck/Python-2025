
#Definimos nuestra variable (Def) y lista es el nombre del parametro
def sumar_lista(lista):
    #Sum es sumar y return devuelve el resultado
    return sum(lista)

# y aqui el resultado es la suma de la lista que es 1 + 2 + 3 + 4 + 5
resultado = sumar_lista([1, 2, 3, 4, 5])
print (resultado)

print ("Este es otro paso")

def sumar_lista(lista):
   #Creamos variable con 0 ya que no tenemos nada
    total = 0
    #Aqui es un bucle for, le dice para cada elemento haz lo siguiente
    for numero in lista:
        #Y aqui el total lo suma por numero
        total += numero
    return total

print(sumar_lista([1,2,3,4,5]))

print ("Ahora veremos un valor maximo")
#Lo mismo definimos nuestra variable
def mayor(lista):
    #Y aqui le regresa el valor maximo de la variable lista
    return max(lista)

print (mayor([8,2,10,15,100,1000000,2,5,34]))

def contar_vocales(palabra):
    #Aqui definimos las vocales
    vocales = "aeiouAEIOU"
    #Y le damos a nuestro contador un valor de 0
    contador = 0
# Y aqui si letra en la la variable palabra tiene vocales devolvera su valores y si tiene mas de 1 lo sumara
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

print(contar_vocales("abecedario"))

palabra = input("Escribe una palabra: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print("Número de vocales:", contador)
