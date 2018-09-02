'''
Faça um Programa para um caixa eletrônico. O programa
deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis
serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e
o máximo de 600 reais. O programa não deve se preocupar com a
quantidade de notas existentes na máquina.
- Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de
1;
- Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10, uma nota de
5 e quatro notas de 1.
'''
print("Informe o valor do saque")
saque = float(input())

if saque >= 10 and saque <= 600:
    nota100 = saque // 100
    resto = saque % 100
    print(f'{nota100} notas de 100')
    n50 = resto // 50
    resto = resto % 50
    print(f'{n50} notas de 50')
    n10 = resto // 10
    resto = resto % 10
    print(f'{n10} notas de 10')
    n5 = resto // 50
    resto = resto % 5
    print(f'{n5} notas de 5')
    print(f'{resto} notas de 1')
else:
    print("valor nao permitido")



