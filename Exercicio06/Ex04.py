"""
Defna a função prodnlista que recebe como argumento uma lista de inteiros e
devolve o produto dos seus elementos
"""


def prodnlista(list):

    if len(list) == 0:
        return 1
    else:
        return list[len(list) - 1] * prodnlista(list[:-1])






print(prodnlista([2,3,4]))
print(prodnlista([2,3]))

