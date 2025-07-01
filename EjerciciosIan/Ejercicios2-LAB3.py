alumno = {
    "nombre": "Lucas",
    "rut": "12.345.678-9",
    "notas": (5.5, 4.3, 6.0),
    "ramos_aprobados": {"Matemáticas", "Lenguaje"},
    "plan": "premium"
}

alumno["notas"] = list(alumno["notas"])


alumno["notas"].append(5.8)
print(alumno)
update