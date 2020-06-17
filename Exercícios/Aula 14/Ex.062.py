end = 0
while end != 2:
    pa = int(input('Digite o termo da P.A.: '))
    ra = int(input('Digite o razão da P.A.: '))
    so = pa + ra
    st = 0
    n = 0
    ter = 0
    print(so,end=' ')
    while n < 9:
        n += 1
        so += ra
        st += so
        print(f'{so} ',end='')
    print(f'\nA P.A. é de {pa} é {so} o soma da P.A. é {st}')
    end = int(input('Selecione a operação\n [1] Mostrar mais termos\n [2] Encerrar programa\n'))

