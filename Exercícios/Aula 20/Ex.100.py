from random import randint
from time import sleep


def sorteia(numeros):
    for s in range(0,5):
        n = randint(1,10)
        numeros.append(n)
        print(f'{n} ', end='',flush=True)
        sleep(.5)

# def sorteia(lista):
#     print('Sorteando 5 valores da lista: ',end='')
#     for cont in range(0,5):
#         n = randint(1,10)
#         lista.append(n)
#         print(f'{n} ',end='',flush=True)
#         sleep(0.3)
#     print('PRONTO!')


lista = []
sorteia(lista)

def somaPar(ls):
    soma = 0
    for k in ls:
        if k % 2 == 0:
            soma += k
    print(f'\nA soma de números pares é {soma}')

somaPar(lista)













####### Funcionando
# for s in range(0,5):
#     numeros.append(randint(1,10))
# print(numeros)

# for k in numeros:
#     if k % 2 == 0:
#         soma += k
# print(soma)
# sorteia()
# somaPar()
####### Funcionando