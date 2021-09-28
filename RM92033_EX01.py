# Calculadora de Calorias
alimento = ''
sair = ''
qtd_calorias = 0
qtd_alimento_soma = 0
qtd_calorias_total = 0

print('Seja bem-vindo a Calculadora de Calorias')

while sair != 'SIM':
    alimento = input('Qual alimento foi consumido? ')
    qtd_alimento = input('Qual a quantidade ingerida desse alimento? ')
    qtd_calorias = input('Qual a quantidade de calorias desse alimento? ')
    sair = input('Você deseja sair? Sim ou Não? ').upper()
    qtd_calorias_total = int(qtd_calorias_total) + int(qtd_calorias) * int(qtd_alimento)
    qtd_alimento_soma = int(qtd_alimento_soma) + int(qtd_alimento)

print(f'Foram ingeridas {qtd_calorias_total} calorias e {qtd_alimento_soma} alimentos')
