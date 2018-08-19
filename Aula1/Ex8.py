""" Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês, sabendo-se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo:
 + Salário Bruto : R$
 - IR (11%8 : R$
 - INSS (8%8 : R$
 - Sindicato ( 5%8 : R$
 = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido. """

value_per_hour = float(input("Quanto você ganha por hora ?"))

amount_hour = int(input("Quantas horas você trabalha por mês ?"))

salary_without_tax = value_per_hour * amount_hour

tax_IR = (11/100) * salary_without_tax

tax_INSS = (8/100) * salary_without_tax

syndicate = (5/100) * salary_without_tax

salary_with_tax = salary_without_tax - tax_IR - tax_INSS - syndicate

print("Salário Bruto %d" %(salary_without_tax))

print("Imposto de renda %d " %(tax_IR))

print("Desconto do INSS %d" %(tax_INSS))

print("Desconto Sindical %d" %(syndicate))

print("Salário Liquido total %d" %(salary_with_tax))
