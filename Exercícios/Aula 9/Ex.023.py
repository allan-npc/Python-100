ns = input('Digite um valor de 0 a 9999: ')
ni = int(ns)
# Escrever os valores dos digitos em separado (String)
print(f'String\nUnidade: {ns[3:4]} \nDezena: {ns[2:3]} \nCentena: {ns[1:2]} \nMilhar: {ns[:1]} ')

# Escrever os valores dos digitos em separado (Matemáticamente) 7654
print(f'\nMatemáticamente\nUnidade: {ni // 1 % 10} \nDezena: {ni // 10 % 10} \nCentena: {ni // 100 % 10} \nMilhar: {ni // 1000 % 10} ')