l1 = float(input('Digite o 1º lado: '))
l2 = float(input('Digite o 2º lado: '))
l3 = float(input('Digite o 3º lado: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('{}, {} e {} formam um triângulo...'.format(l1, l2, l3))
    if l1 == l2 and l2 == l3:
        print('     ...EQUILÁTERO!')
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('     ...ESCALENO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('     ...ISOSCELES!')
else:
    print('{}, {} e {} não formam um triângulo!'.format(l1, l2, l3))

