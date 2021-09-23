# Calculadora de Calorias
alimento = ''
sair = ''
qtd_calorias = 0
qtd_alimento_soma = 0

while sair != 'Sim':
    alimento = input('Qual alimento foi consumido? ')
    qtd_alimento = input('Qual a quantidade ingerida desse alimento? ')
    resposta = input('Qual a quantidade de calorias desse alimento? ')
    sair = input('Você deseja sair? Sim ou Não? ')
    qtd_calorias = int(qtd_calorias) + int(resposta) * int(qtd_alimento)
    qtd_alimento_soma = int(qtd_alimento_soma) + int(qtd_alimento)

print(f'Foram ingeridas {qtd_calorias} calorias e {qtd_alimento_soma} alimentos')
