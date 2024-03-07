from random import random
import datetime
aleatorio = random()
# print(aleatorio)
# print(round(aleatorio*10))


def randomico(param):
    return round(aleatorio * param)


data = datetime.datetime(
    randomico(2024), randomico(12), randomico(31),
    randomico(24), randomico(60), randomico(60))
print(data)
