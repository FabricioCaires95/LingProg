"""
Defna a função prodnlista que recebe como argumento uma lista de inteiros e
devolve o produto dos seus elementos
"""


def prodnlista(list):

    if len(list) == 1:
        return len(list)
    else:
        return list[len(list) - 1] * prodnlista(prodnlista(list[len(list) - 2]))






print(prodnlista([2,3,4]))


