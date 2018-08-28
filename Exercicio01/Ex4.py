""" Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius. C = (5 * (F328
/ 98. """

temperature = float(input("Informe a temperatura em  Farenheit"))

convertToCelsius = (5 * (temperature - 32 ) / 9)

print("A temperatura em graus celsius é " + str(convertToCelsius))
