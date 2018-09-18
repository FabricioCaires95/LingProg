"""
6 Espião: Escreva uma função que receba uma lista de
inteiros e retorne True se contém um 007 em ordem, mesmo
que não contínuo. Exemplo:
espiao([1,2,4,0,0,7,5]) --> True
espiao([1,0,2,4,0,5,7]) --> True
espiao([1,7,2,4,0,5,0]) --> False

"""

def f(numeros):
    status = 'Nada'
    for simbolo in numeros:
        if simbolo == 0:
            if status == 'Nada':
                status = 'Zero'
            elif status == 'Zero':
                status = 'Zero1'
        else:
            if simbolo == 7:
                if status == 'Zero1':
                    print('true')
                    return True

    print(status)
    return False

f([1, 7, 3, 0, 0, 3, 7])