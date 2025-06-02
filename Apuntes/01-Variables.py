"""GUIA INICIAL DE PYTHON"""
#Definimos las variables
nombre = "Ian"
apellido = "Fack"
edad = "22"
#Utilizando variables
print ("Hola mi nombre es:", nombre, "y mi apellido es:" , apellido, "mi edad es:", edad)

#print con operador de concatenacion
print ("Hola mi nombre es:" + nombre + "y mi apellido es:" +  apellido + "mi edad es:", edad)

#Print con f-strin
print (f"Hola mi nombre es {nombre} y mi apellido es {apellido} y mi edad es {edad}" )

#Inicializando multiples variables en una sola linea NO RECOMENDADO"
ciudad, region, pais = "Castro", "Los lagos", "Chile"

print (f"y soy de {ciudad}, {region}, {pais}")
