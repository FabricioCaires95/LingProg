"""
2 Mesma letra: Escreva uma função que receba uma string com duas palavras e
retorne True se ambas palavras começarem com a mesma letra. Exemplo:
mesma_letra('Cão covarde') -> True
mesma_letra('Vira Lata') -> False

"""

def mesma_letra(palavra):
    duas_palavras = palavra.split(" ")

    if duas_palavras[0][0].upper() == duas_palavras[1][0].upper():
        return  True
    else:
        return False


print(mesma_letra("Cao covarde"))
print( mesma_letra("Fabricio fabricio"))
