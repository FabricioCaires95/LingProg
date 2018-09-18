"""
1 Menor de dois pares: Escreva uma função que retorne o menor de dois números
dados se ambos os números forem pares, mas retorna o maior se um dos dois for
ímpar. Exemplo:
menor_de_dois_pares(2,4) --> 2
menor_de_dois_pares (2,5) --> 5
"""

def menor_par(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            print(f'O menor par {x}')
        elif y < x:
            print(f'O menor par e {y}')
        else:
            print("Os dois numeros sao pares e iguais ")
    elif x % 2 != 0 or y % 2 != 0:
        if x > y:
            print(f'O Maior Numero e o {x}')
        else:
            print(f'O Maior Numero e o  {y}')



menor_par(3,6)
menor_par(4,2)