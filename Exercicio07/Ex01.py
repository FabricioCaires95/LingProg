"""
1 Defna a função somannat que recebe como argumento um número natural n
 e devolve a soma de todos os números naturais até n.
"""

somannat = lambda n: 1 if n==1 else n + somannat(n-1)

assert(somannat(3) == 2)
print(somannat(2))