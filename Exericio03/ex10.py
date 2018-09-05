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
três notas de 100, uma nota de 50, quatro notas de .
'''
print("Informe o valor do saque")
saque = int(input())


if saque >= 10 and saque <= 600:
    n100 = saque // 100
    r100 = saque % 100
    n50 = r100 // 50
    r50 = r100 % 50
    n10 = r50 // 10
    r10 = r50 % 10
    n5 = r10 // 5
    r5 = r10 % 5
    n1 = r5 // 1

    print(f'Notas de 10: {n100}')
    print(f'Notas de 50: {n50}')
    print(f'Notas de 5: {n5}')
    print(f'Notas de 1: {n1}')
else:
    print("Valor inválido")



