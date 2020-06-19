n_barato = ''
barato = 10000
r = 's'
total = maior = 0
while r not in 'Nn':
    name = input('Digite o nome do produto: ')
    price = float(input('Digite o valor do produto: '))
    total += price
    if price > 1000:
        maior += 1
    if price < barato:
        barato = price
        # print(barato)
        n_barato = name
        # print(n_barato)
    r = input('Deseja continuar? [S/N]\n')
print(f'O total gasto foi de {total}.\n {maior} produtos custam mais de R$1000.00.\n {n_barato} foi o produto mais barato.')