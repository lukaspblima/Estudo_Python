print('Sequenciador Fibonacci')
n = int(input('Digite o número de termos: '))
a = 0
b = 1
if n == 1:
    print(a,'.')
elif n == 2:
    print('{}, {}.'.format(a, b))
elif n > 2:
    print('{}, {},'.format(a, b), end=' ')
    for d in range(1, n-1):
        c = a+b
        print(c, end=', ')
        a = b
        b = c
else:
    print('Que pena, você não verá a sequência.')