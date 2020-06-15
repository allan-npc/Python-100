from math import fabs as fabs
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r1 < fabs(r2 - r3):
    print('Não é possível formar um triangulo, r1 é muito pequeno')
elif r2 < r1 + r3 and r2 < fabs(r1 - r3):
    print('Não é possível formar um triangulo, r2 é muito pequeno')
elif r3 < r1 + r2 and r3 < fabs(r1 - r2):
    print('Não é possível formar um triangulo, r3 é muito pequeno')
else:
    print('A reta é possível')