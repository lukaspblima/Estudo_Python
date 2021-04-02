from random import randint
from time import sleep
print('-'*26)
print('  Sorteie qualquer coisa  ')
print('-'*26)
lista = []
n = int(input(('Digite a quantidade de opções: ')))
while n == 1:
    print('Você não está levando isso a sério...\n  Tente novamente!')
    n = int(input(('Digite a quantidade de opções: ')))
    if n == 1:
        print('Ninguém merece... Mais uma vez!')
        n = int(input(('Digite a quantidade de opções: ')))
        if n == 1:
            print('Desisto de você!')
            sleep(3)
            exit()
print()
c = 1
while c <= n:
    item = input('Digite o {}° item: '.format(c))
    lista.append(item)
    c = c +1
print()
sort = randint(0, n-1)
print('O sorteado foi: {}!'.format(lista[sort]))
print()
print()
input('Aperte ENTER para sair.')