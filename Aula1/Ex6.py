""" Faça um Programa que peça 2 números inteiros e um número
real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo. """

int_number1 = int(input("Informe o primeiro inteiro"))

int_number2 = int(input("Informe o segundo inteiro"))

result1 = (2 * int_number1) * (int_number2 / 2)

print("O prodiuto do dobro do primeiro com metade do segundo " + str(result1))