

tablero = {
    #Fila 1
        "a1": "TorreB",
        "b1": "CaballoB",
        "c1": "AlfilB",
        "d1": "ReinaB",
        "e1": "ReyB",
        "f1": "AlfilB",
        "g1": "CaballoB",
        "h1": "TorreB",

    #Fila 2 #Bucle anidado 
    ** {f"{columna}2":"PeonB" for columna in "abcdefgh"},

    #Fila 7
    ** {f"{colu}7" : "PeonN" for colu in "abcdefgh"},

    #Fila 8
        "a8": "TorreN",
        "b8": "CaballoN",
        "c8": "AlfilN",
        "d8": "ReinaN",
        "e8": "ReyN",
        "f8": "AlfilN",
        "g8": "CaballoN",
        "h8": "TorreN",
}

# B mapa de simbolos dic = simbolos pieza => Caracter

simbolos = {
        #Blanco
        "TorreB" : "R",
        "CaballoB": "N",
        "AlfilB": "B",
        "ReinaB" : "Q",
        "ReyB": "K",
        "PeonB": "P",
        
        #Negro
        "TorreN" : "r",
        "CaballoN": "n",
        "AlfilN": "b",
        "ReinaN" : "q",
        "ReyN": "k",
        "PeonN": "p",
}

#Mostra tablero por cada turno

def mostrar_tablero(tablero):
    print("  a b c d e f g h")
    for fila in range(8,0,-1):
        filastr = f"{fila} "
        for col in "abcdefgh":
            clave = f"{col}{fila}"
            pieza = tablero.get(clave, ".")
            simbolo = simbolos.get(pieza, ".")
            filastr += simbolo + " "
        print(filastr)

piezas_capturadas = []

while True:
    mostrar_tablero(tablero)

    print("------Movimiento de la pieza------")
    casilla_de_origen = input("Ingresa la casilla de origen (ej: e2,a1,etc): ").lower() #Ponemos lower para que todas las letras esten en minusculas
    casilla_de_destino = input("Ingresa la casilla a la que quieres moverte:(ej: e6,a3,etc) ").lower()

    if casilla_de_origen not in tablero:
        print("No hay esa pieza en esa casilla, intentalo nuevamente porfavor :) \n")
        continue

    pieza = tablero[casilla_de_origen] #Aqui usaremos el diccionario de tablero y le daremos la casilla de origen
    casilla_de_destino = tablero.get(casilla_de_destino) #Aqui buscara la pieza que se eligio

    if casilla_de_destino:
        if (pieza[-1] == "B" and casilla_de_destino[-1] == "N") or \
        (pieza[-1] == "N" and casilla_de_destino [-1] == "B"):
            piezas_capturadas.append(casilla_de_destino) 
            print(f"Capturaste la {casilla_de_destino} en {casilla_de_destino.upper()}")
        else:
            print("No puedes capturar tu propia pieza")
            continue

    tablero[casilla_de_destino] = pieza
    del tablero[casilla_de_origen]

    print("\n----Tablero actualizado :) ----")
    mostrar_tablero(tablero)

    if piezas_capturadas:
        print("\n Piezas capturadas")
        print(" ".join(simbolos[p] for p in piezas_capturadas))
    
    break #Para jugar mas veces se puede eliminar este break







