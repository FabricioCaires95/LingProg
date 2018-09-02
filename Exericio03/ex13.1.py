'''13. Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; '''

nome = input(("Insira o nome (maior que três caracteres): "))
while len(nome) <= 3:
    nome = input("Insira o nome (maior que três caracteres): ")

idade = int(input("Insira a idade (0 - 150): "))
while idade < 0 or idade > 150:
    idade = int(input("Insira a idade (0 - 150): "))

salario = int(input("Insira o salário (maior que zero): "))
while salario <= 0:
    salario = int(input("Insira o salário (maior que zero): "))

sexo = input("Insira o sexo (f/m): ")
while not (sexo in ['f', 'm']):
    sexo = input("Insira o sexo (f/m): ")

estadocivil = input("Insira o estado civil (s/c/v/d): ")
while not (estadocivil in ['s', 'c', 'v', 'd']):
    estadocivil = input("Insira o estado civil (s/c/v/d): ")