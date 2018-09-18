"""
5 Blackjack: Faça uma função que receba 3 inteiros entre 1 e 11. Se a soma deles for
menor que 21, retorne o valor da soma. Se for mair do que 21 e houver um 11,
subtraia 10 da soma antes de apresentar o resultado. Se o valor da soma passar de
21, retorne ‘ESTOUROU’. Exemplo:
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'ESTOUROU'
blackjack(9,9,11) --> 19

"""

def vinte_um(x, y, z):

    soma = x + y + z

    if soma <= 21:
        return print(f'{x},{y},{z} -> {soma}')
    else:
        if x == 11 or y == 11 or z == 11:
            soma -= 11
            return print(f'{x},{y},{z} -> {soma}')
        return print("ESTOUROU")


print(vinte_um(5,6,7))
print(vinte_um(9,9,9))
print(vinte_um(9,9,11))

print(vinte_um(10,9,5))