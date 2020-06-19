lista = []
par = []
impar = []
for r in range(0,7):
    n = int(input('Digite o número: '))
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)
lista.append(par[:])
lista.append(impar[:])
print(lista)
print(f'par {par}')
print(f'impar {impar}')
print(f'Organizada par{par}')
print(f'Organizada impar {impar}')