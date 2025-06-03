#Se pueden agregar diferentes tipos de datos en un diccionario
paciente = {
        "Nombre":"Carlos",
        "Apellido":"Santana", #El primero es la clave, el 2do el valor y son un puro elemento no 2
        "Edad": 50,
        "Ciudad":"Quellón",
        "Region":"De los lagos",
        "Consultas" : [14,20,40],
        "Diagnostico" : ("Resfrio")
}
print(type(paciente))

medico = dict(
    nombre = "Ian",
    Apellido = "Fack",
    edad = 22,
    Ciudad = "Chonchi"
)

print(paciente)
print(medico)
print (medico["nombre"])

del(paciente["Nombre"])
print(paciente)
