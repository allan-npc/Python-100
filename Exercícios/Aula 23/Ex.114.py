import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br').getcode()
except:
    print('O site Pudim não está online')
else:
    print('O site Pudim está online')

