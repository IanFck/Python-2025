print ("Bienvenido a la tienda, ¿que deseas comprar? \n 1:Mostrar productos disponibles, \n 2:Agregar productos, 3: Eliminar productos")

Inventario = {
        "Platano": 200,
        "Manzana": 20,
        "Uvas": 80

}

opcion = str(input("Ingresa tu opcion 1,2,3 o Salir"))
while True:
    if opcion == "1":
        print("Mostrar productos disponibles")
    if Inventario:
        for i in Inventario:
            cantidad = Inventario.get(i)
            print(f"{i} / cantidad: {cantidad}")
        else:
            print
    elif opcion == "2":
        print("Ingresa el nombre del producto")
        nombre = str(input("> "))
        print("Ingresa ")
        print("Agregar productos")
    elif opcion == "3":
        print("Elinando productos")
    elif opcion == "Salir":
        print("Has elegido Salir")




