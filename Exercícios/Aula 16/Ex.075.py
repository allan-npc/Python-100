# for n in range(0,4):
#     n = int(input('Digite os valores: '))
nt = (int(input('Digite os valores: ')), int(input('Digite os valores: ')), int(input('Digite os valores: ')), int(input('Digite os valores: ')))
# print(n)
print (nt)
print(f'O número 9 apareceu {nt.count(9)}')
if 3 in nt:
    print(f'O número 3 foi o {nt.index(3)+1}° número digitado.')
else:
    print('O número 3 não foi digitado nenhuma vez')
print('Os números pares digitados são: ')
for p in nt:
    if p % 2 == 0:
        print(p, end='')
# print(f'{nt%2==0}')