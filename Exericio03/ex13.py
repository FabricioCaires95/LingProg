'''
13. Faça um programa que peça uma nota, entre zero e dez. Mostre
uma mensagem caso o valor seja inválido e continue pedindo até
que o usuário informe um valor válido
'''

print("Informe uma nota entre dez e zero")

nota = float(input())

while nota < 0 or nota > 10:
    print("Valor invalido")
    nota = float(input())
else:
    print("valor ok")