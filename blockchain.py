from functools import reduce
from collections import OrderedDict
from hash_util import hash_string_256, hash_block
MINNING_REWARD = 10
genesis_block = {
    'previou_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
blockchain = [genesis_block]
transacoes_abertas = []
owner = 'Ginhu'
participants = {'Ginhu'}


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(transacoes_abertas, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in transacoes_abertas
                      if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
        if len(tx_amt) > 0 else tx_sum + 0,
        tx_sender, 0)
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['receiver'] == participant] for block in blockchain]
    amount_received = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
        if len(tx_amt) > 0 else tx_sum + 0,
        tx_recipient, 0)
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
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
    # transaction = {
    #     'sender': sender,
    #     'receiver': recipient,
    #     'amount': amount
    # }
    transaction = OrderedDict(
        [('sender', sender), ('receiver', recipient), ('amount', amount)])
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
        if not valid_proof(
                block['transactions'][:-1],
                block['previou_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINNING',
    #     'receiver': owner,
    #     'amount': MINNING_REWARD
    # }
    reward_transaction = OrderedDict(
        [('sender', 'MINNING'),
         ('receiver', owner), ('amount', MINNING_REWARD)])
    copied_transactions = transacoes_abertas[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previou_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
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
    print('balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
else:
    print('Finalizando programa!')

print('Finalizado')
