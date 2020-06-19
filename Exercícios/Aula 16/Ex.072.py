nt = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n1 = 30
while n1 not in range(0,21):
    n1 = int(input('Tente novamente.\nDigite um número de 0 à 20: '))
print(f'Você digitou o número {nt[n1-1].title()}.')