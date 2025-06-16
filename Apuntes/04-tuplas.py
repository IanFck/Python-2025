#Tupla de estudiantes
estudiantes = ("Samir", "Ivan", "Ian","Antonio")
print  (estudiantes)

print ("Ahora veremos las tuplas")
#Las tuplas no se pueden modificar y eliminar
#CREANDO UNA TUPLA
tupla = tuple ()
estudiantes2 = ("Samir", "Ivan", "Ian")
frutas = []
print (estudiantes2)
print (type (tupla))
print (type (frutas))

print (estudiantes2.index ("Ivan"))

#estudiantes.pop() esto no se puede porque la tupla no se puede modificar
#print(estudiantes)
#estudiantes = ("Pablo")

#Index indica la posicion del elemento
print(estudiantes.index ("Samir"))
print (estudiantes)

#Sorted ordena elementos en una tupla
print(sorted(estudiantes)) #Y tambien lo transforma en una lista

