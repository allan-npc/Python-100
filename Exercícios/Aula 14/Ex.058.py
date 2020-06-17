import random
n1 = random.randrange(0,10)
# print(n1)
n2 = int(input('Digite um palpite: '))

while n1 != n2:
    n2 = int(input('Errou, tente mais uma vez: '))
print(f'Acertou, o numero sortado foi {n1}')