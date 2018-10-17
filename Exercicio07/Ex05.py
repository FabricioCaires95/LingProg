"""
5 Defna a função contemnpar que recebe como argumento uma lista de números
inteiros o e devolve True se o contém um número par e False em caso contrário.
Ex: contemnpar ([2,3,1,2,3,4]) = True
Ex: contemnpar ([1,3,5,7]) = False
"""

contempar = lambda list: False if len(list) == 0 or (list[len(list)-1]) % 2 != 0 and not contempar(list[:-1]) else True

print(contempar([2,3,1,2,3,4]))
print(contempar([1,3,5,7]))