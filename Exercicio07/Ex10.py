"""
10 Defna a função inverteLista que recebe como argumento uma lista o e devolve a
mesma lista mas invertda.
Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
Ex: inverteLista([])
"""

inverteLista = lambda list: list[::-1] if len(list) > 0 else []

print(inverteLista([1,2,3,4,5]))
print(inverteLista([]))