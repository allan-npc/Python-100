v = int(input('Qual valor quer sacar: '))
total = v
r50 = 50
r10 = 10
r5 = 5
r1 = 1
t50 = t10 = t5 = t1 = 0
while total > r50:
    total -= r50
    t50 += 1
    if total < r50:
        while total > r10:
            total -= r10
            t10 += 1
    if total < r10:
        while total > r5:
            total -= r5
            t5 += 1
    if total < r5:
        while total > 0:
            total -= r1
            t1 += 1
    
print(f'total 50: {t50}')
print(f'total 10: {t10}')
print(f'total 5: {t5}')
print(f'total 1: {t1}')
print (f'Total: {total}')