from random import randint
from time import sleep
print('Descubra o número secreto!')
r = randint(1, 5)
c = 0
while c != 'N':
    n = int(input('Digite um número de 1 à 5: '))
    print('...')
    sleep(1)
    if n == r:
        print('=== Parabéns, você acertou! ===')
    else:
        print('Você errou! Tente outra vez.')
    c = input('Deseja continuar? [S/N]: ').upper()
    print('--------------------------')
    if c == 'S' and n == r:
        r = randint(1, 5)
input('\n Aperte ENTER para sair.')
