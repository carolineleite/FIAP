# Primeiro importamos o módulo sys
import sys
# Depois criamos algumas variáveis de exemplo
nome = "Bruce Wayne"
idade = 30
peso = 92.3
# Vamos exibir em uma mensagem o nome da variável, o tipo (type) e o tamanho (getsizeof)
print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

# Primeiro importamos o módulo sys
import sys
# Agora vamos criar uma lista vazia
lista = []
# E verificar o tamanho
print("O objeto lista é do tipo {} e tem {} bytes".format(type(lista), sys.getsizeof(lista)))

# Criação de uma tupla com as categorias dos Jedi
categorias = ("Youngling", "Padawan", "Knight", "Master")

# Exibindo a tupla inteira -> ('Youngling', 'Padawan', 'Knight', 'Master')
print(categorias)

# Exibindo o segundo item da tupla -> Padawan
print(categorias[1])

# Usando um índice negativo para exibir o último item da tupla -> Master
print(categorias[-1])

# Exibindo cada item da tupla usando um loop
for categoria in categorias:
    print(categoria)

# Importando o módulo sys para conseguirmos usar o getsizeof
import sys

# Criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()

# Printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))