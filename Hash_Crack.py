import crypt

salt = input("Insert the salt here: ")
wordlist_path = input ('Insert the path to Wordlist: ')
with open(wordlist_path, 'r') as wordlist:
    for line in wordlist:
        line = line.strip()
        hashed_line = crypt.crypt(line, crypt.METHOD_SHA512)
        print(hashed_line)

senha = input ("Digite a senha para criptografar: ")
hashx = crypt.crypt(senha,salt)
print(hashx)
