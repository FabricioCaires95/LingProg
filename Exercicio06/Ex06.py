"""6 Defina a função todos_imparesQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém apenas números ímpares e False em caso contrário.
 Ex: todos_imparesQ([1,3,5,7]) = True
 Ex: todos_imparesQ([]) = True
 Ex: todos_imparesQ([1,2,3,4,5]) = False """

def todos_imparesQ(list):
    return True if len(list) == 0 else True if list[len(list) - 1] % 2 != 0 and todos_imparesQ(list[:-1]) else False


print(todos_imparesQ([]))
print(todos_imparesQ([1,3,5,7]))
print(todos_imparesQ([1,2,3,4,5]))
