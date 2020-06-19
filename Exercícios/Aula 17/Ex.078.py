n = 0
lv = []
maior = 0
menor = 11
for v in range(0,5):
    n = int(input('Digite os valores: '))
    lv.append(n)
    if maior < n:
        maior = n
    if menor > n:
        menor = n
print(f'O maior valor foi {maior} na posição {lv.index(maior)} e o menor valor {menor} na posição {lv.index(menor)}')