"""
Defna a função div que recebe como argumentos dois números naturais m
 e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não
pode recorrer às operações aritmétcas de multplicação, divisão e resto da divisão
inteira.
"""

def div(x, y):
    return 0 if x < y else 1 + div(x - y, y)



print(div(10,5))
print(div(5,10))