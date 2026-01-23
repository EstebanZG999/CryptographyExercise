def xor_binario(mensaje, clave):
    mensaje = mensaje.strip().replace(" ", "")

    for c in mensaje:
        if c != "0" and c != "1":
            raise ValueError("La cadena del mensaje debe contener solo 0s y 1s")
        
    if len(clave) < len(mensaje):
        raise ValueError("La clave debe ser al menos tan larga como el mensaje")
    
    resultado = ""

    for i in range(0, len(mensaje)):
        bits_mensaje = mensaje[i]
        bits_clave = clave[i]

        if bits_mensaje == bits_clave:
            resultado += "0"
        elif bits_mensaje != bits_clave:
            resultado += "1"

    return resultado


mensaje = "10101010"
clave   = "11001100"
esperado = "01100110"
resultado = xor_binario(mensaje, clave)
print("Mensaje:   ", mensaje)
print("Clave:     ", clave)
print("Resultado: ", resultado)
print("Esperado:  ", esperado)
print("Se obtuvo lo esperado:", resultado == esperado)
print()

cifrado = xor_binario(mensaje, clave)
descifrado = xor_binario(cifrado, clave)
print("Cifrado:   ", cifrado)
print("Descifrado:", descifrado)
print("Se obtuvo lo esperado:", descifrado == mensaje)