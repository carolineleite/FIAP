"""
Loop While

resposta = ''

while resposta != '42':
    resposta = input('Qual a resposta para a vida, o universo e tudo mais? ')

print('Parabéns, você é um verdadeiro Geek!')

numero = 1

while numero % 2 == 1:
    numero = int(input("Digite um número par: "))

print('Você conseguiu!')


contadora = 0

while contadora <= 10:
    print(contadora)
    contadora = contadora + 1

n = int(input('De qual número você quer a tabuada? '))
i = 1

# Tabuada
while i <= 10:
    print("{} x {} = {}" .format(n, i, n * i))
    i = i + 1
"""

for x in range(1, 51, 2):
    print(x)


