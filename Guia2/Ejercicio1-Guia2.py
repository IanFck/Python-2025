#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 1
try:
    Palabra = input("Ingrese el parrafo :")

#El parrafo que se ingresara sera : “El Proyecto Integrador del primer semestre, se evaluará y desarrollará en 3 asignaturas en conjunto  Taller de Introducción a la Ingeniería donde trabajarán el desarrollo práctico del proyecto, Habilidades Comunicativas donde desarrollarán las habilidades de presentación y redacción y por
#último Programación, donde aplicarán técnicas para codificar y diseñar el software del proyecto.”
    if not Palabra: #Aqui estamos diciendo que si el texto esta vacio, tendra un error y dara un mensaje de "El texto no puede estar vacio"
        raise ValueError("El texto no puede estar vacio")

    Palabra_minuscula_mayuscula = Palabra.lower() #Aqui cambiaremos la variable para que todas las palabras esten en minuscula

    Lista = (list(Palabra_minuscula_mayuscula.split())) #Aqui separaremos la lista con todas las palabras ingresadas del parrafo
    print (Lista)

    Palabra_a_buscar = input("Dime una palabra a buscar: ").lower() #Aqui le pediremos al usuario una palabra a buscar
    
    buscar = Lista.count(Palabra_a_buscar) #Y aqui imprimiremos cuantas veces se repite la palabra ingresada
    
    print("La palabra aparece:",buscar, "veces")

except ValueError as error: #Aqui almacenaremos value error en la variable error
    print("Error:", error)


