n1 = int(input('Digite um valor inteiro: '))
op = int(input('Digite 1 para conversão binária, 2 para conversão octal e 3 para hexadecimal\n'))

if op == 1:
    print(f'{n1:04b}')
elif op == 2:
    print(f'{n1:06o}')
else:
    print(f'{n1:4X}')