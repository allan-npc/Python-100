def maior(* num):
    zero = 0
    print('-='*30)
    print('Analisando os valores passados...')
    print(f'{num} Foram informados {len(num)} valores ao todo.')
    sorted(num)
    print(f'{num} Foram informados {len(num)} valores ao todo.')


maior(4, 2, 7, 5, 9, 10, 15)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()