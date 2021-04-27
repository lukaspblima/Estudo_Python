from random import randint
from time import sleep
print('\033[34m-=-\033[m'*15)
print('\033[33m       Jogue Jokenpô contra a máquina!\033[m')
print('\033[34m-=-\033[m'*15)
j = int(input('Escolha [1] Pedra, [2] Papel, [3] Tesoura: '))-1
jokenpo = ['Pedra', 'Papel', 'Tesoura']
m = randint(0, 2)
sleep(1)
print('     \033[36mVocê\033[m : {} X {} : \033[31mA Máquina\033[m'.format(jokenpo[j], jokenpo[m]))
if (j==0 and m==2) or (j==1 and m==0) or (j==2 and m==1):
    print('             Você ganhou!')
elif (j==0 and m==1) or (j==1 and m==2) or (j==2 and m==0):
    print('         Que pena, você perdeu!')
elif j==m:
    print('       Incrível, houve um empate!')
