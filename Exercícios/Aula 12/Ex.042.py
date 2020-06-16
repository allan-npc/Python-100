r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < (r2 + r3) and r1 < abs(r2 - r3):
    print('Não é possível formar um triangulo, r1 é muito pequeno')
elif r2 < (r1 + r3) and r2 < abs(r1 - r3):
    print('Não é possível formar um triangulo, r2 é muito pequeno')
elif r3 < (r1 + r2) and r3 < abs(r1 - r2):
    print('Não é possível formar um triangulo, r3 é muito pequeno')
else:
    print('O triângulo é possível')

if r1 == r2 and r2 == r3:
    print('Será formado um triângulo equilatero')
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('Será formado um triângulo escaleno')
else:
    print('Será formado um triângulo isósceles')