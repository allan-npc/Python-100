lv = []
for val in range(0,5):
    n = int(input('Digite o valor: '))
    if val == 0 or n > lv[-1]:
        lv.append(n)
    else:
        pos = 0
        while pos < len(lv): # Enquanto a posição for menor que o tamanho da lista
            if n <= lv[0]: # Se o número for menor ou igual ao número da posição 0 da lista
                lv.insert(pos, n) # Adicione o valor na posição mais baixa registrada
                break
            pos += 1    
print(lv)