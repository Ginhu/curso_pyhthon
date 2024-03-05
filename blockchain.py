# Comentário
blockchain = []


def ultimo_elemento():
    """Retorna o ultimo valor da lista blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def adicionar_novo(valor_transacao, ultimo_elemento=[1]):
    """Adiciona um novo valor a lista blockchain
    Argumentos:
        valor_transacao: valor a ser adicionado
        ultimo_elemento: ultimo elemento da lista (padrao = [1])
    """
    if ultimo_elemento is None:
        ultimo_elemento = [2]
    blockchain.append([ultimo_elemento, valor_transacao])


def valor_da_transacao():
    """Retorna o valor inserido pelo usuario"""
    entrada_usuario = float(input('Por favor entre um novo valor: '))
    return entrada_usuario


def pegar_escolha_usuario():
    entrada_usuario = input('Please choose: ')
    return entrada_usuario


def imprimir_valores_blockchain():
    for bloco in blockchain:
        print('Imprimindo bloco')
        print(bloco)
    else:
        print('-' * 20)


def verificar_cadeia():
    # block_index = 0
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


condicao_do_loop = True

while condicao_do_loop:
    print('Por favor escolha.')
    print('1: Adicionar uma nova transação')
    print('2: Retornar os blocos da blockchain')
    print('h: Manipular o blockchain')
    print('p: Parar')
    escolha_usuario = pegar_escolha_usuario()
    if escolha_usuario == '1':
        valor_transacao = valor_da_transacao()
        adicionar_novo(valor_transacao, ultimo_elemento())
    elif escolha_usuario == '2':
        imprimir_valores_blockchain()
    elif escolha_usuario == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [3]
    elif escolha_usuario == 'p':
        condicao_do_loop = False
    else:
        print('Por favor escolha uma opção válida')
    if not verificar_cadeia():
        print(imprimir_valores_blockchain())
        print('Blockchain inválida')
        break
else:
    print('Finalizando programa!')

print('Finalizado')
