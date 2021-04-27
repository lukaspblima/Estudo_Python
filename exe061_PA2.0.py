print('Progressão Aritmética 2.0')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
pa = n1
c = 1
while c <= 10:
    print(pa, end=' ')
    pa += n2
    c += 1
    print('->' if c <= 10 else '', end=' ')
