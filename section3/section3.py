# Tarefa 1
lista_nomes = ['guga', 'lucas', 'gabi', 'giNhu', 'sergio', 'nice']

for nome in lista_nomes:
    """Tarefa 1"""
    # print(len(nome))

    """Tarefa 2 e 3"""
    if len(nome) > 5 and ('n' in nome or 'N' in nome):
        print(len(nome))

# Tarefa 4
condicional = True
while condicional:
    lista_nomes.pop()
    if len(lista_nomes) == 0:
        condicional = False
print('finalizado')
