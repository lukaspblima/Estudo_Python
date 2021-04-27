a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))
if a>b>c:
    print('{} é o MAIOR número e {} o MENOR.'.format(a, c))
elif a>c>b:
    print('{} é o MAIOR número e {} o MENOR.'.format(a, b))
elif b>a>c:
    print('{} é o MAIOR número e {} o MENOR.'.format(b, c))
elif b>c>a:
    print('{} é o MAIOR número e {} o MENOR.'.format(b, a))
elif c>a>b:
    print('{} é o MAIOR número e {} o MENOR.'.format(c, b))
elif c>b>a:
    print('{} é o MAIOR número e {} o MENOR.'.format(c, a))
