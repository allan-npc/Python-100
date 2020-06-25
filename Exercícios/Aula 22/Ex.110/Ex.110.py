import moedas
p = float(input('Digite o preço: R$ ').replace(',','.'))
moedas.resumo(p,80,35)

# print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
# print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
# print(f'Aumentando 10%, de {moedas.moeda(p)} temos {moedas.aumentar(p, 10, True)}')
# print(f'Reduzindo 13%, de {moedas.moeda(p)} temos {moedas.diminuir(p, 13, True)}')