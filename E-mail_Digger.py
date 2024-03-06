import os

def busca_arquivos(diretorio, palavras_chave):
    for nome_arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
            try:
                with open(os.path.join(diretorio, nome_arquivo), 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.read()
            except UnicodeDecodeError:
                with open(os.path.join(diretorio, nome_arquivo), 'r', encoding='ISO-8859-1') as arquivo:
                    conteudo = arquivo.read()
            if all(palavra_chave not in conteudo for palavra_chave in palavras_chave):
                print(nome_arquivo)

# Solicita ao usuário o diretório e as palavras-chave
diretorio = input("Insira o diretório: ")
palavras_chave = input("Insira as palavras-chave, separadas por espaço: ").split()

# Chama a função com os inputs do usuário
busca_arquivos(diretorio, palavras_chave)

