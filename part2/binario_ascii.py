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

binario = "01001000011011110110110001100001"

print("Binario a ASCII: " + binario_ascii(binario))