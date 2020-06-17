pa = int(input('Digite o termo da P.A.: '))
ra = int(input('Digite o razão da P.A.: '))
so = pa + ra
st = 0
n = 0
print(so,end=' ')
while n < 9:
    n += 1
    so += ra
    st += so
    print(f'{so} ',end='')
print(f'a P.A. é de {pa} é {so} o total da P.A. é {st}')