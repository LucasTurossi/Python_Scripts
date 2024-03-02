import hashlib

text = input("Insira o valor que você quer transformar em hash: ")

print()

# Converte a string em bytes
text_bytes = text.encode()

# Calcula o hash MD5
md5_hash_object = hashlib.md5(text_bytes)
md5_hex_dig = md5_hash_object.hexdigest()
print(f"MD5 Hash: {md5_hex_dig}")

print()

# Calcula o hash SHA256
sha256_hash_object = hashlib.sha256(text_bytes)
sha256_hex_dig = sha256_hash_object.hexdigest()
print(f"SHA256 Hash: {sha256_hex_dig}")

print()

# Calcula o hash SHA512
sha512_hash_object = hashlib.sha512(text_bytes)
sha512_hex_dig = sha512_hash_object.hexdigest()
print(f"SHA512 Hash: {sha512_hex_dig}")
