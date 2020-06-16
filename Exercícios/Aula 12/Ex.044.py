valor = int(input('Digite o valor do produto: '))
pay_type = int(input('Digite o tipo de pagamento:\n 1. para Dinheiro\Cheque\n 2. para Cartão\n 3. para 2x no cartão\n 4. para 3x ou mais\n'))

if pay_type == 1:
    print(f'O valor a ser pago é de R${valor*0.90}')
elif pay_type == 2:
    print(f'O valor a ser pago é de R${valor*0.95}')
elif pay_type == 3:
    print(f'O valor a ser pago é de R${valor}')
else:
    print(f'O valor a ser pago é de R${valor*1.20}')