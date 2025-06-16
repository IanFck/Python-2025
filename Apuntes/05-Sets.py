#Ahora veremos los sets, no estan ordenadas y no se puede tener duplicados
#Creando sets
colores = {"Azul","Rojo","Azul","Verde"}
otro_color = {"Azul","Naranjo"}

print(colores)

diferencia = colores.difference(otro_color)
print(diferencia)

#Agregando un nuevo elemento
colores.add ("Blanco")
print(colores)

#Eliminado un elemento del set
colores.discard("Blanco")
print(colores)

conjunto_vacio = set()
print (type(conjunto_vacio))

colores = {"Azul", "Rojo", "Verde", "Azul", 34}
print (colores)