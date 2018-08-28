"""Escreva um programa que conta a quantidade de vogais em uma
string e armazena tal quantidade em um dicionário, onde a chave é
a vogal considerada"""


print("entre com uma palavra")
frase = input()

frase = frase.lower()
vogais = 'baioe'
dicionario = {i: frase.count(i) for i in vogais if i in frase}
print(dicionario)