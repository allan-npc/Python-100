n = int(input('Quer ver a tabuada de qual valor? '))
while n > -1:
    m = 0
    print('-' * 30)
    while m != 10:
        m += 1
        print(f'{m} * {n} = {n*m}')
    print('-' * 30)
    n = int(input('Quer ver a tabuada de qual valor? '))
print('Tabuada negativa não né filhão')