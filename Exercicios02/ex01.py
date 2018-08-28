
"""Crie um programa que recebe uma lista de números e
- retorne o maior elemento
- retorne a soma dos elementos
- retorne o número de ocorrências do primeiro elemento da lista
- retorne a média dos elementos
- retorne o valor mais próximo da média dos elementos
- retorne a soma dos elementos com valor negativo
- retorne a quantidade de vizinhos iguais"""

list = []

def negativos(number):
    if number < 0:
        return  True
    else:
        return False


for i in range(5):
    list.append(int(input("Informe um elemento inteiro")))


print("Maior Elemento ", max(list))
print("Soma dos elementos", sum(list))
print("Primeiro elemento da lista", list[0])
print("Media dos elementos ", sum(list) // 5)
print("Valor mais prox da media")
negativo = filter(negativos, list)
print("Soma dos elementos negativos", sum(negativo))
print("Quantidade de vizinhos iguais")