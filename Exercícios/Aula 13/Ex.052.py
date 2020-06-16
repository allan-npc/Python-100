n = int(input('Digite o número a ser verificado: '))
t = 0
for p in range(1,n+1):
    if n % p == 0:
        t += 1
if t == 2:
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')