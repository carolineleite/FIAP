def perguntar():
    return input('O que deseja realizar?\n' +
              '<I> - Para Inserir um usuário: \n' +
              '<P> - Para pesquisar um usuário: \n' +
              '<E> - Para Excluir um usuário: \n' +
              '<L> - Para Listar um usuário: ').upper()


def inserir(dicionarios):
    return dicionario[input('Digite o login: ').upper()], \
           [input('Digite o nome: ').upper(),
            input('Digite a última data de acesso: ').upper(),
            input('Qual a última estação acessada: ').upper()]
