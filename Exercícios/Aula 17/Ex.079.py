fim = 's'
lv = []
while fim not in 'Nn':
    val = int(input('Digite os valores únicos: '))
    fim = input('Deseja continuar [S/N}: ').strip()
    if fim not in 'SsNn':
        fim = input('Deseja continuar [S/N}: ').strip()
    if val not in lv:
        lv.append(val)
lv.sort()
print(lv)