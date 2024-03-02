import base64

text = input("Digite o texto para encode: ")

# Converte a string em bytes
text_bytes = text.encode()

# Codifica os bytes em base64
encoded_bytes = base64.b64encode(text_bytes)

# Converte os bytes codificados em uma string
encoded_str = encoded_bytes.decode()

print(encoded_str)
