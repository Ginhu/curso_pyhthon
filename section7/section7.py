import json
import pickle


def salvar_dados(dados, tipo):
    if tipo == 'p':
        with open('dados.p', mode='wb') as f:
            f.write(pickle.dumps(dados))
    elif tipo == 'txt':
        with open('dados.txt', mode='w') as ft:
            ft.write(json.dumps(dados))


def ler_dados(tipo):
    with open('dados.p', mode='rb') as f:
        dados_p = pickle.loads(f.read())
    with open('dados.txt', mode='r') as ft:
        dados_t = json.loads(ft.read())

    if tipo == 'txt':
        return dados_t
    elif tipo == 'p':
        return dados_p


condicao_loop = True

while condicao_loop:
    print('1: Entrada de dados no arquivo .txt')
    print('2: Entrada de dados no arquivo .p')
    print('3: Ler dados do arquivo .txt')
    print('4: Ler dados do arquivo .p')
    print('q: Sair')

    escolha = input('Faça sua escolha: ')
    if escolha == '1':
        dados_salvos = ler_dados('txt')
        print(dados_salvos)
        dados = input('Digite um nome: ')
        dados_salvos.append(dados)
        salvar_dados(dados_salvos, 'txt')
    elif escolha == '2':
        dados_salvos = ler_dados('p')
        dados = input('Digite um nome: ')
        dados_salvos.append(dados)
        salvar_dados(dados_salvos, 'p')
    elif escolha == '3':
        print('-' * 20)
        print('Dados arquivo .txt: ', ler_dados('txt'))
    elif escolha == '4':
        print('-' * 20)
        print('Dados arquivo .p: ', ler_dados('p'))
    elif escolha == 'q':
        print('Finalizando programa!')
        condicao_loop = False

print('Finalizado com sucesso!')
