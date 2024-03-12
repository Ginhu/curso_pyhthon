objeto = {
    'primeiro': 'primeiro',
    'segundo': 123
}


class Car:
    def __init__(self, param=100):
        self.unit = param

    def __repr__(self):
        return self.unit


print(Car)
lista = [1, 2, 3]
# objeto['primeiro'] = 'Ginhu'
# print(objeto['primeiro'])
# print(lista[-1])
