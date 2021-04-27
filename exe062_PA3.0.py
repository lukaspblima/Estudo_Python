print('Progressão Aritmética 3.0')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
pa = n1
c = 1
x = ''
cont = 10
while x != 0:
    while c <= cont:
        print(pa, end=' ')
        pa += n2
        c += 1
        print('->' if c <= cont else '', end=' ')
    x = int(input('\nAcrescentar mais termos? ([0] para sair): '))
    if x != 0:
        cont += x
    else:
        print('Foram mostrados {} termos'.format(cont))
