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

#for nome in nomes:
#    print(f'O nome do personagem é: {nome}')

male = generos.count('male')
print(f'A quantidade de personagens homens é: {male}')

female = generos.count('female')
print(f'A quantidade de personagens mulheres é: {female}')

nao_se_aplica = generos.count("n/a")
print(f'A quantidade de personagens com gênero que não se aplica é: {nao_se_aplica}')

hermaphrodite = generos.count('hermaphrodite')
print(f'A quantidade de personagens com gênero hermafrodita é: {hermaphrodite}')

none = generos.count('none')
print(f'A quantidade de personagens sem gênero é: {none}')