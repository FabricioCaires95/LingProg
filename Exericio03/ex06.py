'''
Faça um Programa que leia um número e exiba o dia
correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
digitar outro valor deve aparecer valor inválido.
'''

dias_semana = {'1':'Domingo', '2': 'Segunda', '3':'Terça', '4':'Quarta', '5': 'Quinta', '6': 'Sexta', 'Sabado':'7'}

print("Diga um numero ")

numero = input()

if numero in dias_semana:
    print(f'O dia da semana é {dias_semana[numero]}')
          