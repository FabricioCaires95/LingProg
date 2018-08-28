"""Faça um programa que receba duas listas e retorne True se têm
os mesmos elementos ou False caso contrário
Duas listas possuem os mesmos elementos quando são compostas
pelos mesmos valores, mas não obrigatoriamente na mesma ordem"""

list1 = []
list2 = []

print("Lista 1")

for i in range(3):
    list1.append(int(input()))

print("Lista 2")

for i in range(3):
    list2.append(int(input()))

list1.sort()
list2.sort()

equal = (list1 == list2)

if (equal):
    print("possuem os mesmos elementos")
else:
    print("Nao tem elementos em comum")

