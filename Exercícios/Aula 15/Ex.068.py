from random import randrange
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
n = int(input('Digite um valor: '))
pi = input('Par ou Ímpar [P/I] ').capitalize()
pc = randrange(0,5)
r = ''
count = 0
while r != 'ÍMPAR':
    if (n+pc) % 2 == 0:
        r = 'PAR'
        count += 1
    else:
        r = 'ÍMPAR'
        break
    print(f'Você jogou {n} e o computador jogou {pc}. O total deu {n + pc} DEU {r}')
    print('VOCÊ VENCEU!\n Vamos jogar novamente')
    print('=-' *15)
    n = int(input('Digite um valor: '))
print(f'Você jogou {n} e o computador jogou {pc}. O total deu {n + pc} DEU {r}')
print(f'VOCÊ PERDEU!\n GAME OVER! Você venceu {count} vez')
print('=-' *15)