inventario = {
    "pan": {"precio": 800, "cantidad": 10},
    "leche": {"precio": 1200, "cantidad": 5},
    "huevos": {"precio": 150, "cantidad": 30}
}

print(inventario.keys())

for productos, valor in inventario.items():
    total = valor["precio"] * valor["cantidad"]
    print(f"{valor} es el total de {productos}")

producto_mas_caro = max(inventario.items(), key=lambda item: item[1]["precio"])
nombre, datos = producto_mas_caro

print(f"\nEl producto más caro es '{nombre}' con un precio de ${datos['precio']} por unidad.")

animal = input("Dame un animal ")

match animal:
    case "perro":
        print("Hace guau")
    case "gato":
        print("Hace miau")
    case _:
        print("Animal no reconocido")
