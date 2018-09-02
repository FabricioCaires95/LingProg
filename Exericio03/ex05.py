'''
As Organizações Tabajara resolveram dar um aumento de salário
aos seus colaboradores e lhe contrataram para desenvolver o
programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o
aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento
'''

print("Informe o salario atual do funcionario")

salario = float(input())

if salario <= 280:
    percent = 0.2
elif salario > 280 and salario < 700:
    percent = 0.15
elif salario > 700 and salario < 1500:
    percent = 0.10
elif salario > 1500:
    percent = 0.05

valor_aumento = salario * percent
novo_salario = salario + valor_aumento

print("Salario antes do reajuste", salario)
print("percentual de reajuste", percent)
print("Valor do aumento", valor_aumento)
print("Novo salario apos o aumento", novo_salario)