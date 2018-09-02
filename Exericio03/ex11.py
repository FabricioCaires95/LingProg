'''
Faça um programa que faça 5 perguntas para uma pessoa
sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no fnal emitir uma classifcação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classifcada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
contrário, ele será classifcado como "Inocente".
'''

pontos  = 0
respostas= [
    input("Telefonou para a vítima? (s/n): "),
    input("Esteve no local do crime? (s/n): "),
    input("Mora perto da vítima? (s/n): "),
    input("Devia para a vítima? (s/n): "),
    input("Já trabalhou com a vítima? (s/n): ")
]

for resposta in respostas:
    if resposta == "s":
        pontos += 1

if pontos == 2:
    print("Suspeita")
elif pontos >= 3 and pontos <= 4:
    print("Cúmplice")
elif pontos == 5:
    print("Assassino")
else:
    print("Inocente")