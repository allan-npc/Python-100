n = int(input('Digite o número, 999 para parar: '))
count = 0
soma = 0
maior = 0
menor = 100
while n != 999:
    count += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    n = int(input('Digite o número, 999 para parar: '))
print(f'A média dos valores digitados foi {soma/count}.\n O maior valor foi {maior} e o menor {menor}.')