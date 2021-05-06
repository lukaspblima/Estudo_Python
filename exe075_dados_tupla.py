"""a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))
d = int(input('Digite o 4º número: '))
tupla = (a, b, c, d)"""
# não tava errado, mas aqui vai a forma corrigida:
tupla = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))
print(f'Aparições do nº 9: {tupla.count(9)}')
for x in range(0, 5):
    if tupla[x] == 3:
        ok = True
        if ok == True:
            print(f'Posição do nº 3: {x}')
            break
        else:
            print('O nº 3 não foi inserido.')
t = 0
print(f'Número(s) par(es) inserido(s): ', end='')
while t < len(tupla):
    if tupla[t]%2 == 0:
        print(tupla[t], end='; ')
    t +=1