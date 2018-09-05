'''
4 -  Faça um Programa que leia três números e mostre-os em ordem decrescente
'''

list = []

print("primeiro numero ")
v1 = int(input())

list.insert(0, v1)

v2 = int(input())

list.insert(1, v2)

v3 = int(input())

list.insert(2, v3)


print(list)

'''
Solucao do professor
list = [int(x) for x in input(digite os numeros separados por espaco),split()]
'''