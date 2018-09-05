'''
Faça um Programa que peça os 3 lados de um triângulo. O
programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois
lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
'''

print("Insira o primeiro lado")
l1 = float(input())

print("Insira o segundo lado:")
l2 = float(input())

print("Insira o terceiro lado:")
l3 = float(input())

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3:
        print("Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Nao podem formar um triangulo")