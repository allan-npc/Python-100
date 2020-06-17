n1 = int(input('Digite o número de iterações para sequenciar: '))
n2 = 0 #soma 1
n3 = 1 #soma 2
r = 0
fim = 0
while n1 > fim:
    fim +=1
    r = (n2+n3)
    n3 = n2
    n2 = r
    print(f'{n2} + {n3} = {r}')
print('Fim')