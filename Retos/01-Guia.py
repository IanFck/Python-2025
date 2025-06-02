#Aqui le dejaremos un mensaje al usuario para que nos de los grados para calcular
print ("Hola, te calculare una temperatura en Fahrenheit y Kelvin")
Celcius = input("Indicame la temperatura en grados celcius")

RespuestaC = float(Celcius) #Aqui lo cambiamos a float para asi poder hacer operaciones matematicas

F = RespuestaC * 9/5 + 32 #Esto de aqui es la operacion de transformacion de celcius a Fahrenheit
print (round(F , 2)) #Y aqui se ocupa round para redondear el resultado y lo limito en un maximo de 2 decimales

K = RespuestaC + 273.15 #Aqui es la operacion de transformacion de Celcius a Kelvin

print (round(K , 2))


