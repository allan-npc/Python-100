def leiaDinheiro(valor):
    ok = False
    while not ok:
        msg = input(valor)
        if msg.isalpha():
            print(f'ERRO: \"{msg}\" é um valor inválido')
        else:
            ok = True
            return float(msg.replace(',','.'))