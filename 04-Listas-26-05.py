#Comandos para confirmar cambios en github
#git add. / git add.
#git commit -m ""
#git push

#FUNCION LEN (es la cantidad de caracteres que te da una variable)
carrera = "Ingenieria Civil en informatica"
print (f"La palabra {carrera}", len (carrera))

#Valores BOOLEANOS
#True y False
ampolleta = False
Interruptor = True

print (ampolleta, Interruptor)

#Type permite saber el tipo de dato
print (type(Interruptor))

#Comparativa de valores logicos
print (1<10)
print (100<=20)
print (100==100)
#Es False ya que no es el mismo tipo de dato
print (100=="100")
print ("-------------------------------------------")
print (bool (0))
print (bool (1))
print (bool (""))
print (bool ("Hola")) #Da true porque tiene algo dentro del ()
print ("-------------------------------")
print ("AHORA VEREMOS LO QUE SON LISTAS :)")
#En las listas se pueden poner datos duplicados
lista1 = ["Ian", 22, True, "A"]
print (lista1)

#Lista vacia
frutas = []

#LISTA DE SOLO NUMEROS
numero = [1,2,3,4,5,6,7,8]
print (numero)

#LISTA DE SOLO STRING
ramos = list(["Programacion","Programacion", "Introduccion a la ingenieria", "Matematicas", "Quimica", "Habilidades comunicativas"])
print (ramos)

estudiantes = ["Matias", "Juanito", "Cristobal", "Camilo", "Diego"]
print (estudiantes)
#Se imprime solo la primera opcion ya que es una lista
print (estudiantes[0])

print (ramos.count("Programacion"))

print ("Ahora veremos las tuplas")
#Las tuplas no se pueden modificar y eliminar
#CREANDO UNA TUPLA
tupla = tuple ()
estudiantes2 = ("Samir", "Ivan", "Ian")
print (estudiantes2)
print (type (tupla))
print (type (frutas))

print (estudiantes2.index ("Ivan"))

#Ahora veremos los sets, no estan ordenadas y no se puede tener duplicados

conjunto_vacio = set()
print (type(conjunto_vacio))

colores = {"Azul", "Rojo", "Verde", "Azul", 34}
print (colores)