# NOME: Caroline da Silva Leite
# CURSO: Banco de Dados
# Atividade: Manipulação de JSON

import json


def ler_json() -> object:
    with open("star_wars.json", "r", encoding='utf-8') as arquivo:
        return json.load(arquivo)


data = ler_json()

nomes = [d['name'] for d in data]
generos = [d['gender'] for d in data]

for nome in nomes:
    print(f'O nome do personagem é: {nome}')

for genero in generos:
    print(f'O gênero é: {gerero}')



