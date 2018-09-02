'''
2 - Faça um programa que verifique se uma letra digitada é vogal ou consoante
'''

vogais = ['a', 'e' , 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

print("Digite uma letra")

letra = input()

if letra in vogais:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante ')

    