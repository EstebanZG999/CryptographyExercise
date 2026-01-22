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

def base64_binario(texto):
    resultado = []
    for c in texto:
        indice = alfa_base64.index(c)
        # print(indice)
        binario = deciman_binario(indice)
        resultado.append(binario)
    return " ".join(resultado)


texto = "aG9sYSBzb3kga291"

print("Base64 a binario: " + base64_binario(texto))