"""
Defna a função contemnparQ que recebe como argumento uma lista de números
inteiros w e devolve True se w contém um número par e False em caso contrário
"""


def contemparQ(list):
    return False if len(list) == 0 else False if list[len(list) - 1] % 2 != 0 and not contemparQ(list[:-1]) else True


print(contemparQ([3,5,7,9]))
print(contemparQ([3,5,4]))