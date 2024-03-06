import base64

# Nome do arquivo codificado em base64
base64_file_name = '/home/n0kk/decode.txt'

# Ler o arquivo base64
with open(base64_file_name, 'r') as file:
    base64_message = file.read()

# Decodificar a string base64
base64_bytes = base64.b64decode(base64_message)
message = base64_bytes.decode('utf-8')

# Escrever o conteúdo decodificado em um novo arquivo
with open('arquivo_decodificado.txt', 'w') as file:
    file.write(message)

print("Arquivo decodificado com sucesso!")

