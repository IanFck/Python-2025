num = 0 #Aqui es un contador donde el while(mientras) dice que si es menor o igual a 100 lo imprimira y despues se sumara x 2
while num <= 100:
    print(num)
    num += 2
    num = num + 2
#while True: #Bucle infinito
    print(num)
    num += 2 

#01 While
edad = 15
num = 0


#while edad < 18: #BUCLE INFINITO
    #print("Eres menor de edad, no puedes manejar")

while num <= 200: #Es similar a el if
    print(num)
    num += 2
else: #Con el else termina el bucle asi se evitan bucles infinitos
    print("Mi condicion es igual o mayor a 200")
print("Segundo bucle terminado")

while True: #Otro bucle infinito
    parametro = input(">")
    if parametro == "exit": #Hasta que se ponga exit "== Es comparar"
        break
    else:
        print(parametro)

num = 0
while num <= 50:
    num += 1
    if num == 40: #Aqui si es igual a 40, se salta el 40 y sigue el codigo
            continue
    print(num)

#For se usa para lista o diccionarios

for i in (1,2,3,4,5,6,7,8,9,10):
 print(i)

for i in range(1,10,2):#Aqui es un rango entre 1 y 10 pero al final te restara 1 en este caso imprime hasta el 9
    print(i)