"""Faça um programa que leia 2 strings e informe o conteúdo delas
seguido do seu comprimento. Informe também se as duas strings
possuem o mesmo comprimento e são iguais ou diferentes no
conteúdo.
Exemplo:
String 1: Brasil Hexa 2018
String 2: Brasil! Hexa 2018!
Tamanho de "Brasil Hexa 2018": 16 caracteres
Tamanho de "Brasil! Hexa 2018!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente. """

string_1 = input("Informe a primeira String")
string_2 = input("Informe a segunda String")

print("Tamanho de %s : %d" %(string_1, len(string_1)))
print("Tamanho de %s : %d" %(string_2, len(string_2)))

if len(string_1) != len(string_2):
    print("As duas strings sao de tamanhos diferentes. ")
else:
    print("As duas strings têm tamanhos iguais.")