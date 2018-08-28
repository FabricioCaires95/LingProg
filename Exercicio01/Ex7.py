""" João Papo-de-Pescador, homem de bem, comprou um
microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50
quilos8 deve pagar uma multa de R$ 4,00 por quilo excedente. João
precisa que você faça um programa que leia a variável peso (peso
de peixes8 e verifque se há excesso. Se houver, gravar na variável
excesso e na variável multa o valor da multa que João deverá pagar.
Caso contrário mostrar tais variáveis com o conteúdo ZERO. """

weight_fish = float(input("Quantidade em KG de peixes "))
difference = 0

if weight_fish > 50:
    difference = weight_fish - 50
    traffic_take = 4 * difference
    print("Você excedeu o limite em %d e pagara multa (em R$) de %d" %(difference,traffic_take))
else:
    print("Você nao excedeu o limite")