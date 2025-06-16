#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 1
Palabra = input("Ingrese el parrafo :") 

#El parrafo que se ingresara sera : “El Proyecto Integrador del primer semestre, se evaluará y desarrollará en 3 asignaturas en conjunto  Taller de Introducción a la Ingeniería donde trabajarán el desarrollo práctico del proyecto, Habilidades Comunicativas donde desarrollarán las habilidades de presentación y redacción y por
#último Programación, donde aplicarán técnicas para codificar y diseñar el software del proyecto.”

Lista = (list(Palabra.split())) #Aqui separaremos la lista con todas las palabras ingresadas del parrafo
print (Lista)
Palabra_a_buscar = input("Dime una palabra a buscar") #Aqui le pediremos al usuario una palabra a buscar
try: 
    buscar = Palabra.count(Palabra_a_buscar.lower())
    print(buscar) 
except ValueError:
    print ("“El texto no puede estar vacío")  
finally:
    print ("Fin del proceso")

#Ejercicio 2
print ("---------------Ejercicio 2----------------")
S = 500





#Ejercicio 3
print ("---------------Ejercicio 3----------------")
Vendedores = {
            "Juan": [100000, 120000, 250000, 80000, 160000],
            "Alvaro":[200000, 60000, 250000, 140000, 90000],
            "Pedro" : [300000, 79000, 140000, 210000, 70000],
}

Ventas_Juan = list((Vendedores["Juan" ]))
ventas_Alvaro = list((Vendedores["Alvaro"]))
ventas_Pedro = list((Vendedores["Pedro"])) 

sueldo_base = 529000

Ventas_semanales_Juan = sum(Ventas_Juan) / len(Ventas_Juan)
Ventas_semanales_Alvaro = sum(ventas_Alvaro) / len(ventas_Alvaro)
Ventas_semanales_Pedro = sum(ventas_Pedro) / len(ventas_Pedro)


print (Ventas_semanales_Juan)
#Ejercicio 4
print ("---------Ejercicio 4-------")

Numero = input("Dame un numero")
impar = 1

#Ejercicio 5
print ("-----------Ejercicio 5--------------")

Tablero = {
            ""


}

#Ejercicio 6
print ("-----------Ejercicio 6---------------")

