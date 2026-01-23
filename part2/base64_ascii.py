tabla_ascii = {
    'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71,
    'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78,
    'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85,
    'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90,

    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
    'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109,
    'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115,
    't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121,
    'z': 122,

    ' ': 32
}

tabla_ascii_inversa = {}

for k in tabla_ascii:
    tabla_ascii_inversa[tabla_ascii[k]] = k

alfa_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def deciman_binario(numero):
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    while len(binario) < 6:
        binario = "0" + binario

    return binario

def binario_decimal(bits):
    valor = 0
    for c in bits:
        valor = valor * 2
        if c == "1":
            valor += 1
    return valor


def binario_ascii(bits):
    resultado = []
    bits = bits.strip().replace(" ", "")

    for c in bits:
        if c != "0" and c != "1":
            raise ValueError("La cadena debe contener solo 0s y 1s")
    
    if len(bits) % 8 != 0:
        raise ValueError("La cadena debe tener una longitud múltiplo de 8")
    
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]   
        decimal = binario_decimal(byte)
        if decimal not in tabla_ascii_inversa:
            raise ValueError("El valor decimal {} no está en la tabla ASCII definida".format(decimal))
        char = tabla_ascii_inversa[decimal]
        resultado.append(char)

    return "".join(resultado)


def base64_bits6(b64):
    b64 = b64.strip().replace(" ", "")
    padding = 0
    if b64.endswith("=="):
        padding = 2
    elif b64.endswith("="):
        padding = 1

    bits6_total = ""

    for c in b64:
        if c == "=":
            continue
        if c not in alfa_base64:
            raise ValueError("Carácter inválido en Base64: {}".format(c))

        indice = alfa_base64.index(c)
        bits6 = deciman_binario(indice)
        bits6_total += bits6

    return bits6_total, padding

def base64_ascii(b64):
    bits6_total, padding = base64_bits6(b64)

    if padding == 1:
        bits6_total = bits6_total[:-2]
    elif padding == 2:
        bits6_total = bits6_total[:-4]

    if len(bits6_total) % 8 != 0:
        raise ValueError("La cadena debe tener una longitud múltiplo de 8")
    
    texto = binario_ascii(bits6_total)

    return texto

texto_base64 = "SG9sYQ=="

print("De base64 a ascii: " + base64_ascii(texto_base64))