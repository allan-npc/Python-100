import random
nr = random.randint(1,5)
# print(nr)
nu = int(input('Adivinhe o número de 1 a 5: '))

if nu == nr:
    print(f'Parabéns, você acertou o número {nu}')
else:
    print(f'Não foi dessa vez, tente de novo.')