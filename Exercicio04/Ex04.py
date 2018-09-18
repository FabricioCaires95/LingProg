"""
 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver
em alguma posição da lista um 3 do lado de outro 3. Exemplo:
tem_33([1,3,3]) --> True
tem_33([1,3,1,3]) --> False
tem_33([3,1,3]) --> False

"""

def has_33(lista):
    status = "null"
    for i in lista:
        if i == 3:
            if status == "null":
                status = "ok"
            elif status == "ok":
                return True

        else:
            if status == "ok":
                status = "null"
    return False

print(has_33([3,2,2]))
print(has_33([3,3,1]))
print(has_33([1,3,3]))
print(has_33([3,1,3]))