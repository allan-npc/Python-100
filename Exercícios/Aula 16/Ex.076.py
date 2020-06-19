l = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)

for i in range(0, len(l)):
    if i % 2 == 0:
        print(f'{l[i]:.<30}', end='')
    else:
        print(f'R$ {l[i]:>5.2f}')
    # print('.'*15-(len(l[1])))