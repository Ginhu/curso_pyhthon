

def primeira():
    print('Que dia bom')


def segunda(arg, *args):
    for argu in args:
        print(arg(argu))


# segunda(primeira)
# segunda(lambda: print('Que dia bom2'))
# segunda(lambda param: print(param * 'Que dia bom 2 '))
# segunda(lambda param: param * 2, 1, 2, 3)


def terceira(arg, *args):
    for argu in args:
        print('resutlado: {:^20.2f}'.format(arg(argu)))


terceira(lambda param: param * 1.15, 1, 2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8)
