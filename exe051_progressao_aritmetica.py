print('Progressão aritmética:')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
pa = n1
for c in range(n1, n1+10):
    print(pa)
    pa += n2
