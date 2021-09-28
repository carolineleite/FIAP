#Este programa calculará o total de calorias ingeridas pelo usuário no presente dia .
#Definindo as variáveis
nome_alimento = ""
qtde_alimento = 0
qtde_caloria = 0
soma_alimento = 0
soma_caloria = 0
sair = ""
#Introdução do programa
nome = input("Digite seu nome: ")
senha = input("Por favor, digite a sua senha: ")
print("Olá {}! Vamos calcular a quantidade de caloridas ingeridas hoje!".format(nome))

#Iniciando processo de loop
while sair != "2":
    nome_alimento = input("Digite o nome do alimento: ")
    qtde_alimento = int(input("Insira a quantidade do alimento: "))
    qtde_caloria = int(input("Insira a quantidade de caloria do alimento: "))
    sair = input("Você deseja inserir mais algum alimento, {}? 1-Sim ou 2-Não?".format(nome))

#Cálculo realizado para a soma da quantidade de calorias ingeridas.
soma_alimento = soma_alimento + qtde_alimento
soma_caloria = soma_caloria + qtde_caloria * qtde_alimento

#Caso o usuário não queria continuar, insira a mensagem abaixo
print ("Foram consumidas {} calorias neste dia, {}.".format(soma_caloria, nome))