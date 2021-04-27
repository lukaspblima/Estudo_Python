n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1+n2)/2
if m < 5:
    print('Média: {}. Reprovação.'.format(m))
elif m > 5 and m < 6.9:
    print('Média {}. Recuperação.'.format(m))
else:
    print('Média {}. Aprovação.'.format(m))
