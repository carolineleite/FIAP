# Calculadora de Média por Número Impar e Par
contador = 0
media_impar = 0
media_par = 0

for x in range(1, 50, 2):
    nota = float(input(f'VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}? '))
    media_impar = media_impar + nota
    contador = contador + 1

media_impar = media_impar / contador
contador = 0

for x in range(2, 51, 2):
    nota = float(input(f'VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}? '))
    media_par = media_par + nota
    contador = contador + 1

media_par = media_par / contador

print(f'A média ímpar é {media_impar}')
print(f'A média par é {media_par}')

if media_impar > media_par:
    print(f"A média dos alunos ímpares é maior que a dos alunos pares e foi de: {media_impar}")
elif media_impar < media_par:
    print(f"A média dos alunos pares é maior que a dos alunos ímpares e foi de: {media_par}")
elif media_impar == media_par:
    print(f"A média dos alunos pares e ímpares é a mesma e foi de:{media_impar}")
