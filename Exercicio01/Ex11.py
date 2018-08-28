"""Faça um programa que solicite a data de nascimento
(dd/mm/aaaa8 do usuário e imprima a data com o nome do mês por
extenso.
Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973.
Obs.: Não use desvio condicional nem loops."""

import datetime

birth = input("Informe sua data de nascimento no formato dia/mes/ano")

year,month,day = map(int, birth.split('/'))

date_type = datetime.date(day, month, year)

date = date_type.strftime('%d/%B/%Y')

day, month,year = map(str, date.split('/'))

print ("Você nasceu em %s de %s de %s" %(day, month,year))