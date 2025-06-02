Palabra = str(input("Ingresa una palabra de maximo 30 caracteres"))  [:30]
Palabra_en_mayuscula = Palabra.upper()
print (Palabra_en_mayuscula) 

Palabra_en_minuscula = Palabra.lower()
print (Palabra_en_minuscula)

print ("Esta es la cantidad de letras a en mayuscula:", Palabra.count ("A"))
print ("Esta es la cantidad de letras a en minuscula:", Palabra.count ("a"))

print ("Esta es la la longitud de tu palabra hecha" , len(Palabra))