"""
# Vídeo Aula
import json

with open("star_wars.json", "r") as arq_json:
    dic = json.load(arq_json)
    for chave, dados in dic.items():
        print(chave + " " + str(dados))
"""
# Usando a função open para criar um objeto do tipo arquivo
arquivo = open("musica_aula_arquivo.txt", "w")

# Verificando o tipo do objeto arquivo
print(type(arquivo))

# Printando o conteúdo do objeto arquivo
print(arquivo)

# Printando uma linha do arquivo
print(arquivo.readline())

# Printando outra linha do arquivo
print(arquivo.readline())
