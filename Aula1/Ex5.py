""" Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit."""

temperature = float(input("Informe a temperatura em celsius"))

convertToFarenheit = (temperature * 1.8) + 32

print("A temperatura em Farenheit é " + str(convertToFarenheit))