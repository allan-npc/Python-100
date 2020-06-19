n = count = soma = 0
while n != 999:
    n = int(input('Digite um número, 999 para parar: '))
    count += 1
    if n == 999:
        break       
    soma += n
    print(soma)
print(f'A quantidade de números digitadas foi {count} com a soma total de: {soma}')