def encriptar(texto, s):
    resultado = ""

    for char in texto:
        if char.isupper():
            resultado += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + s - 97) % 26 + 97)
        else:
            resultado += char

    return resultado

texto = "Hola soy Juan P"
s = 3
print("Texto original: " + texto)
print("Salto: " + str(s))
print("Texto encriptado: " + encriptar(texto, s))
