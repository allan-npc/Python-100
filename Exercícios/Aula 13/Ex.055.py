we_l = []
for p in range(1,6):
    we = int(input(f'Digite o peso da pessoa {p}: '))
    we_l.append(we)
we_l.sort()
print(f'A pessoa mais leve tem {we_l[0]}kg e a mais pesada tem {we_l[4]}kg')