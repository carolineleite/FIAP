lista = [3, 2, 1]

print(sum(lista))


# Função de somar
def somar():
    a = float(input('Digite um valor: '))
    b = float(input('Digite outro valor: '))

    soma = a + b

    print(soma)


somar()


# Função de subtrair
def subtrair(a, b):

    subtrai = a - b

    print(subtrai)


valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))
subtrair(valor1, valor2)


# Função de divisão
def divisao(a, b):
    dividir = a / b
    return dividir

print(divisao(7, 3))
