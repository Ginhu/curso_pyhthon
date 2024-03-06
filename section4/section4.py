lista_pessoas = [
  {'nome': 'Ginhu',
   'idade': 37,
   'hobbies': ['games', 'cozinhar']
   },
  {'nome': 'Flavio',
   'idade': 50,
   'hobbies': ['games', 'aprender']
   }]

lista_nomes = [el['nome'] for el in lista_pessoas]
lista_idades = all([el['idade'] > 20 for el in lista_pessoas])
# copia_lista = lista_pessoas[:]
# copia_lista[0]['nome'] = 'Jose'
copia_lista = [pessoa.copy() for pessoa in lista_pessoas]
copia_lista[0]['nome'] = 'Jose'
a, b = lista_pessoas
p1, p2, p3 = a.items()

print(lista_nomes)
print(lista_idades)
print(lista_pessoas)
print(copia_lista)
print(a)
print(p1)
print(p2)
print(p3)
print(b)
