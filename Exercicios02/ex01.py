
"""Crie um programa que recebe uma lista de números e
- retorne o maior elemento
- retorne a soma dos elementos
- retorne o número de ocorrências do primeiro elemento da lista
- retorne a média dos elementos
- retorne o valor mais próximo da média dos elementos
- retorne a soma dos elementos com valor negativo
- retorne a quantidade de vizinhos iguais"""

list = []


for i in range(5):
    list.append(int(input("Informe um elemento inteiro")))


media = sum(list) // 5
prox = list[0]
diferenca = media - list[0]
menorDif = diferenca

for i in range(len(list)):
    diferenca =  media - i

    if diferenca == 0:
        diferenca = i
    elif diferenca > 0:
        diferenca = diferenca * -1
    elif diferenca < menorDif:
        menorDif = diferenca
        prox = i


soma_negativos = 0

for i in range(len(list)):
    if i < 0:
        soma_negativos += i




print("Maior Elemento ", max(list))
print("Soma dos elementos", sum(list))
print("Primeiro elemento da lista", list[0])
print("Media dos elementos ", sum(list) // 5)
print("Valor mais prox da media", prox)
print("Soma dos elementos negativos", soma_negativos)
print("Quantidade de vizinhos iguais")