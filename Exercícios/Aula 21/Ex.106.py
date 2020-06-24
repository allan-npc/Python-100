def pyhelp(msg):
    welcome = (f"Acessando o manual do comando msn '{msg}'")
    print(f'\033[0;97;44m{"~"*len(welcome)}\n{welcome}\n{"~"*len(welcome)}\033m')
    help(msg)

ajuda = input('Função ou Biblioteca> ')
pyhelp(ajuda)

# \033[m \033[m

# \033[0;30;43m
# \033[m