n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 < n2 and n1 < n3:
    print(f'O menor número é primeiro, {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é segundo, {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número é o terceiro, {n3}')

if n1 > n2 and n1 > n3:
    print(f'O maior número é primeiro, {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é segundo, {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é o terceiro, {n3}')

# Jeito do Allan
# alln = []
# n1 = int(input('Digite o primeiro número: '))
# alln.append(n1)
# n2 = int(input('Digite o segundo número: '))
# alln.append(n2)
# n3 = int(input('Digite o terceiro número: '))
# alln.append(n3)

# print(f'O menor número é {alln[0]} e o maior número é {alln[len(alln)-1]}!')


