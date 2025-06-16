entrada = input("Ingrese un valor entero:")

#ES como correcion de errores, es una forma de corregir errores
try:
    numero = int(entrada)
    print ("Numero ingresado:", entrada)
except ValueError: #Error por tipo de dato
    print("Error de valor: el valor ingresado no es entero")
except ValueError as e:
    print(f"Error inesperado: {e}")#Errores genericos e inesperados
else:
    print("Conversion fue existosa!")
finally: #Accion de limpieza, cierra el archivo si es que esta abierto
    print("Finalizacion del bloque a")

