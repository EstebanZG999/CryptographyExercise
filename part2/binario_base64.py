alfa_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def binario_decimal(bits):
    valor = 0
    for c in bits:
        valor = valor * 2
        if c == "1":
            valor += 1
    return valor

def binario_base64(bits):
    bits = bits.strip().replace(" ", "")

    for c in bits:
        if c != "0" and c != "1":
            raise ValueError("La cadena debe contener solo 0s y 1s")
    
    if len(bits) % 8 != 0:
        raise ValueError("La cadena debe tener una longitud múltiplo de 8")
    
    resultado = ""

    for i in range(0, len(bits), 24):
        bloque = bits [i:i+24]
        len_bloque = len(bloque)
        bytes = len_bloque // 8

        while len(bloque) < 24:
            bloque += "0"
        
        grupo1 = bloque[0:6]
        grupo2 = bloque[6:12]
        grupo3 = bloque[12:18]
        grupo4 = bloque[18:24]

        decimal1 = binario_decimal(grupo1)
        decimal2 = binario_decimal(grupo2)
        decimal3 = binario_decimal(grupo3)
        decimal4 = binario_decimal(grupo4)

        c1 = alfa_base64[decimal1]
        c2 = alfa_base64[decimal2]
        c3 = alfa_base64[decimal3]
        c4 = alfa_base64[decimal4]

        if bytes == 1:
            resultado += c1 + c2 + "=="
        elif bytes == 2:
            resultado += c1 + c2 + c3 + "="
        elif bytes == 3:
            resultado += c1 + c2 + c3 + c4
        else:
            raise ValueError("Bloque de tamaño incorrecto")

    return resultado

bits = "01001000011011110110110001100001"

print("Binario a base64: " + binario_base64(bits))