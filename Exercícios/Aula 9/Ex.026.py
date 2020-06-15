fra = input('Digite sua frase: ').upper()
a = "A"
print(f'A letra A aparece {fra.count(a)} vezes na sua frase')

print(f'A primeira vez que a letra A aparece é na posição {fra.find(a)}')

print(f'A ultima vez que a letra A aparece é na posição {fra.rfind(a)}')


