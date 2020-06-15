sal = int(input('Digite o valor do salário a ser aumentado: '))
if sal > 1250:
    print(f'O salário de R${sal} deverá ser aumentado em 10% para o total de R${sal + (sal/100)*10}')
else:
    print(f'O salário de R${sal} deverá ser aumentado em 15% para o total de R${sal + (sal/100)*15}')