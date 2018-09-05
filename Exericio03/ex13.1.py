'''13. Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; '''

valid = True

while valid:
    nome = input("Digite o nome")
    idade = int(input("Digite a idade"))
    salario = float(input("Digite o salario"))
    sexo = input("Digite o sexo")
    estado_civil = input("Digite o estado civil")

    if len(nome) > 3 and idade >= 0 and idade <= 150 and salario > 0.0 and sexo == "fm" and estado_civil == "scvd":
        print("passsou ")
    else:
        valid = not valid