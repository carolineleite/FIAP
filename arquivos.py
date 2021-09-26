"""
# Vídeo Aula
import json

with open("star_wars.json", "r") as arq_json:
    dic = json.load(arq_json)
    for chave, dados in dic.items():
        print(chave + " " + str(dados))
"""

"""
Conteúdo online
# Usando a função open para criar um objeto do tipo arquivo
arquivo = open("musica_aula_arquivo.txt")

# Verificando o tipo do objeto arquivo
print(type(arquivo))

# Printando o conteúdo do objeto arquivo
print(arquivo)

# Printando uma linha do arquivo
print(arquivo.readline())

# Printando outra linha do arquivo
print(arquivo.readline())

# Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)

# Passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()

# Comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))

# Colocando a lista em ordem alfabética
linhas_do_arquivo.sort()

# Exibindo nossa lista, agora em ordem alfabética
print(linhas_do_arquivo)

# Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
"""

# Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

# usando a função open para criar um objeto do tipo arquivo
arquivo = open("testando_arq.txt", "w")

# Escrevendo o conteúdo da variável conteúdo dentro do arquivo
arquivo.write(conteudo)

# Fechando o arquivo
arquivo.close()

# Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

# Usando a função open para criar um objeto do tipo arquivo
arquivo = open("testando_arq.txt", "a")

# Escrevendo o conteúdo da variável conteúdo dentro do arquivo
arquivo.write(conteudo)

# Fechando o arquivo
arquivo.close()

# Importando o módulo json
import json

# Criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

# Convertendo o dicionário para uma string o formato json
final = json.dumps(contatos)

# Exibindo a string convertida
print(final)
