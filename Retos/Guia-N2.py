#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 1
Palabra = input("Ingrese el parrafo :") 

#El parrafo que se ingresara sera : “El Proyecto Integrador del primer semestre, se evaluará y desarrollará en 3 asignaturas en conjunto  Taller de Introducción a la Ingeniería donde trabajarán el desarrollo práctico del proyecto, Habilidades Comunicativas donde desarrollarán las habilidades de presentación y redacción y por
#último Programación, donde aplicarán técnicas para codificar y diseñar el software del proyecto.”

Lista = (list(Palabra.split())) #Aqui separaremos la lista con todas las palabras ingresadas del parrafo
print (Lista)
Palabra_a_buscar = input("Dime una palabra a buscar") #Aqui le pediremos al usuario una palabra a buscar
buscar = Lista.count(Palabra_a_buscar)
print(buscar)   

#Ejercicio 2
print ("---------------Ejercicio 2----------------")
S = 500





#Ejercicio 3
print ("---------------Ejercicio 2----------------")
Vendedores = {
            "Juan": [100000, 120000, 250000, 80000, 160000],
            "Alvaro":[200000, 60000, 250000, 140000, 90000],
            "Pedro" : [300000, 79000, 140000, 210000, 70000],
}

Ventas_Juan = (Vendedores["Juan" ])
ventas_Alvaro = (Vendedores["Alvaro"])
ventas_Pedro = (Vendedores["Pedro"])
