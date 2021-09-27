# NOME: Caroline da Silva Leite
# CURSO: Banco de Dados
# Atividade: Manipulação de JSON

import json


def ler_json():
    with open("star_wars.json", "r", encoding='utf-8') as arquivo:
        return json.load(arquivo)


data = ler_json()

nomes = [d['name'] for d in data]
generos = [d['gender'] for d in data]
dicionario = dict(zip(nomes, generos))

for personagem, genero in dicionario.items():
    print(f"The character's name is: {personagem} and your gender is {genero}")

male = generos.count('male')
female = generos.count('female')
nao_se_aplica = generos.count("n/a")
hermaphrodite = generos.count('hermaphrodite')
none = generos.count('none')

print(f'A quantidade de personagens homens é: {male}')
print(f'A quantidade de personagens mulheres é: {female}')
print(f'A quantidade de personagens com gênero que não se aplica é: {nao_se_aplica}')
print(f'A quantidade de personagens com gênero hermafrodita é: {hermaphrodite}')
print(f'A quantidade de personagens sem gênero é: {none}')
