Lista = [1,3,2,3,2,3,3,3]
nombres = ["Camilo", "PEPE"]
Lista.insert(3,"Hola")

Nuevalista = list(zip(Lista, nombres))
Lista.extend(nombres)
Lista.pop(1)
print (Lista)

Tupla = ("Ian","Gatio", 3)

#Tupla_ordenada = sorted(Tupla)
#print(Tupla_ordenada)

sets = {4,2,3}
sets.add(10)
set2 = sets.copy()
print (len(sets))

diccionario = {
        "Ian": 22,
        "Programacion": "Aprobado",
        "Cursos aprobados" : ["Matematicas","Bilogia", 1],
        "Tupla": {1,2,3,4,5},

}

print(diccionario["Ian"])
print(diccionario.values())