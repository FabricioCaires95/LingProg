"""
3 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as
palavras na ordem reversa. Exemplo:
mestre_yoda('Eu estou em casa') --> 'casa em estou Eu'
mestre_yoda('Estamos prontos') --> 'prontos Estamos

"""

def reversa(sentenca):

    sentenca_array = sentenca.split(" ")
    print(sentenca_array)
    new_string = ' '.join(sorted(sentenca_array,reverse=True))

    return  new_string



print(reversa("Fabricio santos"))