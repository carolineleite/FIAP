# Cria lista
lista = ['Guitarra', 'Bateria', 'Violão']

print(lista)

# Adiciona elemento na lista com o método input
lista.append(input('Digite o novo instrumento: '))

print(lista)

# Insere um item na lista na posição informada
lista.insert(0, 'Violino')

print(lista)

# Remove último item da lista
lista.pop()

print(lista)

# Remove um determinado elemento da lista
lista.remove('Bateria')
print(lista)

# Tamanho da lista
print(len(lista))

# Saber quantas vezes um elemento está na lista
print(lista.count('Guitarra'))

# Ordena a lista
lista.sort()

print(lista)

# Coloca a lista ao contrário
lista.reverse()

print(lista)
