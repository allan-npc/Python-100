from math import sqrt
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
print(f'A hipotenusa deste triângulo retângulo é: {round(sqrt(ca**2 + co**2),2)}')