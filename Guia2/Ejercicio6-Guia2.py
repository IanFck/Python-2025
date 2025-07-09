#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 6
import time

#reloj digital desde 00:00:00 hasta 23:59:59
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
           