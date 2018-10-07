"""
Defna a função prodnlista que recebe como argumento uma lista de inteiros e
devolve o produto dos seus elementos
"""


def prodnlista(list):
    sizeList = len(list) - 1
    return list[sizeList] if sizeList == 1 else sizeList * prodnlista(list)








print(prodnlista([1,1]))