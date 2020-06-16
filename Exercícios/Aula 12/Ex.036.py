from math import ceil
valor = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do salário: '))
pag = int(input('Digite em quantos anos será pago: '))

sal30 = (sal/100)*30
parc = valor/(pag*12)

if parc >= sal30:
    print(f'As parcelar ultrapassam 30% do seu salário, R${sal30:.2f}, empréstimo negado')
else:
    print(f'Empréstimo aprovado com parcelas no valor de {round(parc,2)} em {pag*12} meses')

# print(sal30, parc, per)