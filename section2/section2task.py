# Tarefa um atribuir a variáveis o nome e idade do usuário
# nome = input('Por favor digite o seu nome: ')
# idade = int(input('Agora por favor digite sua idade: '))

nome_usuario = input('Por favor digite o seu nome: ')
idade_usuario = int(input('Agora por favor digite sua idade: '))


def imprimir_nome_idade():
    """Tarefa dois criar uma função que imprime na tela o nome e a idade
     em uma string apenas"""
    # print('nome: ', nome, '- idade: ', idade)
    print('nome: ', nome_usuario, '- idade: ', idade_usuario)


imprimir_nome_idade()


def imprimir_argumentos(argumento1='Sem argumento', argumento2='Pois é'):
    """Tarefa três criar uma função que imprime na tela os argumentos
        Argumentos:
            argumento1: aceita qualquer argumento (padrão = 'Sem argumento')
            argumento2: aceita qualquer argumento (padrão = 'Pois é')
    """
    print(argumento1, ' - concluindo:', argumento2)


argumento1 = input('Digite aqui seu primeiro argumento: ')
argumento2 = input('Digite aqui seu segundo argumento: ')
imprimir_argumentos()
argumento1 = input('Digite aqui seu primeiro argumento: ')
argumento2 = input('Digite aqui seu segundo argumento: ')
imprimir_argumentos(argumento1, argumento2)


def calculo_de_decadas():
    """Tarefa quatro função que retorna a quantidade de décadas vividas pelo
      usuário"""
    # return idade//10
    return idade_usuario//10


print(calculo_de_decadas())
