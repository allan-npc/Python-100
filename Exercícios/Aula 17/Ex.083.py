ex = input('Digite a expressão: ')
abre = fecha = 0
for par in ex:
    if par == '(':
        abre += 1
    elif par == ')':
        fecha += 1
if abre == fecha:
    print('Sua expressão é válida')
else:
        print('Sua expressão não é válida')