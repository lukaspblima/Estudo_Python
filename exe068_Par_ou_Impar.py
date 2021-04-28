from random import  randint
tit = 'Par ou Ímpar 3.0'
print('=-='*8)
print(f'== {tit:^18} ==')
print('=-='*8)
print('Jogue até perder!')
v = 0
while True:
    maq = randint(0, 10)
    jog = int(input('Insira um número: '))
    poi = input('Par ou Ímpar [P/I]: ')
    while poi not in 'PpIi':
        poi = input('Escolha somente entre Par ou Ímpar [P/I]: ')
    if poi in 'Pp' and (jog+maq)%2 == 0:
        print(f'A Máquina jogou: {maq}!')
        print(f'{jog+maq} é PAR! Você venceu!')
        v += 1
    elif poi in 'Ii' and (jog+maq)%2 == 1:
        print(f'A Máquina jogou: {maq}!')
        print(f'{jog+maq} é ÍMPAR! Você venceu!')
        v += 1
    else:
        print(f'A Máquina jogou: {maq}!')
        print(f'O resultado foi {jog+maq}. Que pena, você perdeu!')
        print(f'Você teve um total de {v} vitórias.')
        break

