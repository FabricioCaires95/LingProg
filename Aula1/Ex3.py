""" Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês. """

value_per_hour = float(input("Qual o valor do seu salário hora ?"));

amount_hour = int(input("Quantas horas você trabalha por mês ?"));

total = value_per_hour * amount_hour

print("Você ganha " + str(total) + " R$ por mês !")