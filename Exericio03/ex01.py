'''
1 - Faça um programa que peça dois números e imprima o maior deles
'''

print("Informe o primeiro numero")
num1 = int(input())

print("Informe o segundo numero")
num2 = int(input())

if (num1 > num2):
    print(f'O maior número é o {num1}')
elif (num2 > num1):
    print(f'O maio número é o {num2}')
else:
    print("Os números são iguais")