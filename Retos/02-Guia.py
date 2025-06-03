#Ejercicio 2
NumeroE = int(input("Ingresa un numero entero"))
NumeroF = float(input("Ingresa un numero decimal"))
NumeroC = complex(input("Ingresa un numero imaginario de esta forma (Ejemplo 3+4j :)"))

Potencia = NumeroC ** NumeroE
print ("Tu resultado en una potencia entre el complejo y entero es :", Potencia)
Suma = NumeroC + NumeroF 
print ("Tu resultado en una suma de entre el complejo y decimal es:", Suma)
Producto = NumeroC * NumeroE 
print ("Tu resultado en una multiplicacion entre el complejo y entero es:", Producto)
Modulo_complejo = abs(Potencia)
print ("Tu resultado absoluto es:", Modulo_complejo)
Rmodulo_complejo = round(Modulo_complejo, 3)
print ("Tu resultado redondeado en decimales es:",Rmodulo_complejo) 

