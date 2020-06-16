f = str(input('Digite a frase: ')).upper()
n = f.replace(" ","")
fi = ''

for p in range(len(n)-1,-1,-1):
    fi += n[p]
if n == fi:
    print(f'A frase "{f.capitalize()}" é um palíndromo')
else:
    print(f'A frase "{f.capitalize()}" não é um palíndromo')