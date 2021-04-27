from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
anohoje = int(date.today().year)
i = anohoje-nasc
if i <= 9:
    print('{} anos. Categoria Mirim'.format(i))
elif i > 9 and i <= 14:
    print('{} anos. Categoria Infantil'.format(i))
elif i > 14 and i <= 19:
    print('{} anos. Categoria Júnior'.format(i))
elif i > 19 and i <= 20:
    print('{} anos. Categoria Sênior'.format(i))
else:
    print('{} anos. Categoria Master'.format(i))
