lista = []
r = 's'
while r not in 'Nn':
    n = int(input('Digite o número: '))
    lista.append(n)
    r = input('Deseja continuar? [S/N]: ')
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Essa é a lista de números em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado')
else:
    print(f'O valor 5 não foi digitado')