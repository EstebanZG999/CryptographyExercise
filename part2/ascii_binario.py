texto = "Hola soy Juan P"
convertidor = " ".join(format(ord(char), '08b') for char in texto)

print("Ascii a binario: " + convertidor)