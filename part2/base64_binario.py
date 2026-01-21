import base64

texto = "Hola soy Juan P"

bytes = texto.encode('ascii')

data = base64.b64encode(bytes)

print(data)

