"""
# Criando dicionário
usuarios = {}
print(usuarios)

# Adicionando itens
usuarios = {
    'chaves': ['Chaves do 8', '24/12/2017', 'Recep_01'],
    'quico': ['Quico das Flores', '20/12/2017', 'Raiox_03']
}
print(usuarios)

# Adicionando mais um item
usuarios['florinda'] = ['Dona Florinda', '24/12/2017', 'Raiox_01']
print(usuarios)

# Separador para pegar um item específico
print('####---####')
print(usuarios.get('quico'))
"""

from funcoes_dic import *

usuarios = {}

opcao = perguntar()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
        opcao = perguntar()

# Um dia eu termino
