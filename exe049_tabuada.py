print('Tabuada, mais uma vez:')
print('Escolha uma opção: [1] Específico.\n                   [2] Geral.')
o = int(input('Sua opção: '))
if o == 1:
    n = int(input('Digite o número a ser calculado: '))
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, c*n))
elif o == 2:
    for c in range(1, 11):
        for t in range(1, 11):
            print('{} x {} = {}'.format(c, t, c*t))
else:
    print('Opção Inválida.')