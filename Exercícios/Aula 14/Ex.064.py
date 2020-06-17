n = int(input('Digite o número, 999 para parar: '))
count = 0
soma = 0
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite o número, 999 para parar: '))
print(f'Foram digitados {count} números com a coma total de {soma}')