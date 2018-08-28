"""Faça um programa que receba duas listas e retorne True se são
iguais ou False caso contrario.
Duas listas são iguais se possuem os mesmos valores e na mesma
ordem."""


list1 = []
list2 = []

print("Lista 1")

for i in range(4):
    list1.append(int(input()))

print("Lista 2")

for i in range(4):
    list2.append(int(input()))


equal = (list1 == list2)

if (equal):
    print("As duas listas sao iguais")
else:
    print("As duas listas sao diferentes")
