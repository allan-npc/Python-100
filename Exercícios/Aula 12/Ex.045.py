import random
player = int(input('Escolha pedra (1), papel(2) ou tesoura(3)'))
pc = random.randrange(1,4)
dic_jok = {1:'Pedra', 2:'Papel', 3:'Tesoura'}

if player == pc:
    print(f'Empatamos')
elif player == 1 and pc == 3:
    print(f'Você me venceu, você jogou {dic_jok.get(player)} e eu joguei {dic_jok.get(pc)}')
elif player == 2 and pc == 1:
    print(f'Você me venceu, você jogou {dic_jok.get(player)} e eu joguei {dic_jok.get(pc)}')
elif player == 3 and pc == 2:
    print(f'Você me venceu, você jogou {dic_jok.get(player)} e eu joguei {dic_jok.get(pc)}')
else:
    print(f'Dessa vez eu venci, você jogou {dic_jok.get(player)} e eu joguei {dic_jok.get(pc)}')
print(pc)