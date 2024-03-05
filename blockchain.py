# Comentário
blockchain = []


def ultimo_elemento():
    """Retorna o ultimo valor da lista blockchain"""
    return blockchain[-1]


def adicionar_novo(valor_transacao, ultimo_elemento=[1]):
    """Adiciona um novo valor a lista blockchain
    Argumentos:
        valor_transacao: valor a ser adicionado
        ultimo_elemento: ultimo elemento da lista (padrao = [1])
    """
    blockchain.append([ultimo_elemento, valor_transacao])


def valor_do_usuario():
    """Retorna o valor inserido pelo usuario"""
    entrada_usuario = float(input('Por favor entre um novo valor: '))
    return entrada_usuario


valor_transacao = valor_do_usuario()
adicionar_novo(valor_transacao)

valor_transacao = valor_do_usuario()
adicionar_novo(ultimo_elemento=ultimo_elemento(),
               valor_transacao=valor_transacao)

valor_transacao = valor_do_usuario()
adicionar_novo(valor_transacao, ultimo_elemento())

print(blockchain)
