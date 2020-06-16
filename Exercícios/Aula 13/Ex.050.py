s = 0
for n in range (1,7):
    n1 = int(input('Digite o número: '))
    if n1 % 2 ==0:
        s += n1
print(f'A soma dos números pares é {s}')