#Guia N°2 Pia Rojas y Ian Fack
#Ejercicio 2
#Aqui analizandolo se vio que es un bucle
S = 0 #Por lo cual empezaremos con un 0
numero1 = 500 
numero2 = 456

while numero1 <= 800: #En este bucle, usaremos for donde recorrera numero 1 hasta llegar a 800
    S += numero1 
    S += numero2 
    numero1 += 10 #Y analizandolo el primer numero tiene un patron y es que el segundo numero se suma por 10
    numero2 -= 2 #Y el segundo se suma 2

print("La sumatoria es:", S)
