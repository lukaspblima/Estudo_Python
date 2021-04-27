print('Calculadora de 2 Números Python')
o = 6
while o == 6:
    n1= float(input('Digite o 1º Número: '))
    n2= float(input('Digite o 2º Número: '))
    print('[1] Somar  [2] Subtrair  [3] Multiplicar  [4] Dividir')
    print('[5] Maior  [6] Novos Números  [7] Sair')
    o= int(input('>>> Operação desejada: '))
    if o == 1:
        print('>> Resultado: {} + {} = {}'.format(n1, n2, n1 + n2))
        r = str(input('Deseja repetir? [S/N]: '))
        if r not in 'Nn':
            o = 6
        else:
            o = 7
    if o == 2:
        print('>> Resultado: {} - {} = {}'.format(n1, n2, n1 - n2))
        r = str(input('Deseja repetir? [S/N]: '))
        if r not in 'Nn':
            o = 6
        else:
            o = 7
    if o == 3:
        print('>> Resultado: {} * {} = {}'.format(n1, n2, n1 * n2))
        r = str(input('Deseja repetir? [S/N]: '))
        if r not in 'Nn':
            o = 6
        else:
            o = 7
    if o == 4:
        print('>> Resultado: {} / {} = {}'.format(n1, n2, n1 / n2))
        r = str(input('Deseja repetir? [S/N]: '))
        if r not in 'Nn':
            o = 6
        else:
            o = 7
    if o == 5:
        if n1 > n2:
            print('>> Resultado: {} é maior que {}'.format(n1, n2))
            r = str(input('Deseja repetir? [S/N]: '))
            if r not in 'Nn':
                o = 6
            else:
                o = 7
        else:
            print('>> Resultado: {} é menor que {}'.format(n1, n2))
            r = str(input('Deseja repetir? [S/N]: '))
            if r not in 'Nn':
                o = 6
            else:
                o = 7
    if o == 7:
        print('Bye Bye!')