from random import randint
from time import sleep
palp = []
jogos = []
print(f'-=-=- {"Palpiteiro MEGA SENA!":^20} -=-=-')
print('---------------------------------')
qtd = int(input('Quantos jogos deseja gerar: '))
for j in range(0, qtd):
    for c in range(0, 6):
        n = randint(1, 60)
        if c == 0:
            palp.append(n)
        elif n in palp:
            n = randint(1, 60)
            palp.append(n)
        else:
            palp.append(n)
    print(f'Jogo {j+1}: {sorted(palp)}')
    sleep(1)
    jogos.append(palp[:])
    palp.clear()
print(f'-=-=- {"BOA SORTE!":^20} -=-=-')