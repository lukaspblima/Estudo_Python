from random import randint
from time import sleep
print('Jogo da Advinhação, de novo')
cont = 'S'
vit = der = 0
while cont not in 'Nn':
    num = randint(1, 5)
    adv = ''
    while adv != 0 and adv != num:
        adv = int(input('Advinhe o número de 1 a 5 (0 para sair): '))
        if adv == num:
            sleep(1)
            vit += 1
            print('Você acertou! Precisou de {} tentativas!'.format(vit + der))
        if adv != num and adv != 0:
            sleep(1)
            der += 1
            print('Você errou! Outra vez...')
    if adv == 0:
        cont = 'N'
    cont = str(input('Deseja reiniciar? [S/N]: '))
if cont == 'N':
    print('Número da vez: ',num)
print('Fim de jogo! \nNúmero de tentativas: {}\nNúmero de Vitórias: {}\nNúmero de Derrotas: {}'.format(vit+der, vit, der))