'''
Uma fruteira está vendendo frutas com a seguinte tabela de
preços:
 Até 5 Kg Acima de 5 Kg
Morango R$ 2,50 por Kg R$ 2,20 por Kg
Maçã R$ 1,80 por Kg R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
sobre este total. Escreva um algoritmo para ler a quantidade (em
Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.
'''

preco = 0.0

print("Quantidade de morango em kg")
morang = float(input())

print("Quantidade de macas em kg ")
maca = float(input())

if maca <= 5:
    total_maca = maca * 1.8
else:
    total_maca = maca * 1.5

if morang <= 5:
    total_morango = morang * 2.5
else:
    total_morango = morang * 2.2

total_kilos = maca + morang
preco = total_maca + total_maca

if total_kilos > 8 or preco > 25 :
    preco = preco * 0.9

print(f'Voce comprou {total_kilos}Kg de maça e morango')
print(f'Pagara o valor de {preco}$')
