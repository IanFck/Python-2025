#Ejercicio 1: Conversión de temperaturas
#Crea un programa que guarde en una constante la temperatura en grados Celsius, y que la convierta a Fahrenheit. Usa variables apropiadas y muestra ambos valores con texto explicativo.

resultado = input("Dame una temperatura en celcius:")

temperaturac = float(resultado) #Se cambia a float porque no te toma el input sin el float al ser un numero (lo cambia de un string a float)
temperaturaf = temperaturac * 1.8 + 32

print("Temperatura en Fahrenheit:", temperaturaf)
print("Temperatura en Celcius:", temperaturac)

print("Este es otra opcion")

temperaturac2 = 15.0
temperaturaf2 = temperaturac2 * 1.8 + 32

print("Temperatura en Celcius:", temperaturac2)
print("Temperatura en Fahrenheit:", temperaturaf2)

#Ejercicio 2: Identificar tipo de dato

#Crea 4 variables con diferentes tipos de datos (int, float, str, bool) y muestra en pantalla qué tipo de dato tiene cada una usando la función type()

datos = "Hola"
datof = 64.5
datoi = 2 
datob = True

print ("Tipo de dato", (type(datos)))
print ("Tipo de dato",(type(datof)))
print ("Tipo de dato",(type(datoi)))
print ("Tipo de dato",(type(datob)))

# Ejercicio 3: Cálculo de área de un círculo
print ("Hola, te calculare el radio de un ejercicio")
respuesta = input("Dame el dato de el radio")

radio = float(respuesta)
pi = 3.1416
area = pi * (radio ** 2)
print(f"El área del círculo es: {area:.2f}") #Lo dejamos asi ya que nos pidieron redondearlo en 2 decimales


#  Ejercicio 4: Calculadora de sueldo semanal
horas_trabajadas = input("Dame tus horas trabajas en la semana")
valor_de_horas = input("Y dame el valor de esas horas")

horas = int(horas_trabajadas)
valor = int(valor_de_horas)

sueldo = valor * horas 
print("Tu sueldo que ganaste en la semana es de:", sueldo)