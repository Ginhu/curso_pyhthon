MINNING_REWARD = 10
genesis_block = {
        'previou_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
transacoes_abertas = []
owner = 'Ginhu'
participants = {'Ginhu'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    open_tx_sender = [tx['amount'] for tx in transacoes_abertas
                      if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['receiver'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def ultimo_elemento():
    """Retorna o ultimo valor da lista blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def adicionar_novo(recipient, sender=owner, amount=1.0):
    """Adiciona um novo valor a lista blockchain
    Argumentos:
        sender: who sends the transaction
        recipient: who receives the transaction
        amount: amount of coins of the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'receiver': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        transacoes_abertas.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def valor_da_transacao():
    """Retorna o valor inserido pelo usuario"""
    tx_recipient = input('Nome do recipient: ')
    entrada_usuario = float(input('Por favor entre um novo valor: '))
    return tx_recipient, entrada_usuario


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previou_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINNING',
        'receiver': owner,
        'amount': MINNING_REWARD
    }
    copied_transactions = transacoes_abertas[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previou_hash': hashed_block,
        'index': len(blockchain),
        'transactions': transacoes_abertas
    }
    blockchain.append(block)
    return True


condicao_do_loop = True

while condicao_do_loop:
    print('Por favor escolha.')
    print('1: Adicionar uma nova transação')
    print('2: Mine new block')
    print('3: Retornar os blocos da blockchain')
    print('4: Output participants')
    print('h: Manipular o blockchain')
    print('p: Parar')
    escolha_usuario = pegar_escolha_usuario()
    if escolha_usuario == '1':
        dados_transacao = valor_da_transacao()
        recipient, amount = dados_transacao
        if adicionar_novo(recipient, amount=amount):
            print('Added Transaction!')
        else:
            print('Transaction failed!')
        print(transacoes_abertas)
    elif escolha_usuario == '2':
        if mine_block():
            transacoes_abertas = []
    elif escolha_usuario == '3':
        imprimir_valores_blockchain()
    elif escolha_usuario == '4':
        print(participants)
    elif escolha_usuario == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previou_hash': 'Rooster',
                'index': 0,
                'transactions': [{
                    'sender': 'Rooster',
                    'recipient': 'Ginhu',
                    'amount': 100.0}]
            }
    elif escolha_usuario == 'p':
        condicao_do_loop = False
    else:
        print('Por favor escolha uma opção válida')
    if not verificar_cadeia():
        print(imprimir_valores_blockchain())
        print('Blockchain inválida')
        break
    print('balance: ', get_balance('Ginhu'))
else:
    print('Finalizando programa!')

print('Finalizado')
