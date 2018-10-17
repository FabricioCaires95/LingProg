"""
3 Defna a função primnalg que recebe como argumento um número natural e
devolve o primeiro algarismo (o mais signifcatvo) na representação decimal de n.
Ex: primnalg(5649) = 5
Ex: primnalg(7) = 7
"""

primalq = lambda n : n if n < 10 else primalq(n // 10)

assert (primalq(5649) == 5)
print(primalq(5649))
print(primalq(700))