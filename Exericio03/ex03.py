'''
Faça um programa para a leitura de duas notas parciais de um
aluno. O programa deve calcular a média alcançada por aluno e
apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual
a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a
dez.
'''

print("Informe a primeira nota")

nota1 = float(input())

print("Informe a segunda nota")

nota2 = float(input())

media = (nota1 + nota2) // 2

print(f' média: {media}')

if media == 10.0:
    print("Aprovado com distinção")
elif media >= 7 and media <= 9.9:
    print("Aluno Aprovado")
elif media < 7 and media >= 0:
    print("Aluno Reprovado")
else:
    print("Media invalida")