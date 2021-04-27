from datetime import date
idade = int(input('Digite o ano do seu nascimento: '))
anohoje = date.today().year
x = int(anohoje-idade)
y = 18-x
z = x-18
if x < 18:
    print('{} anos. Você ainda não está em idade de alistamento. Faltam {} anos, você deverá se alistar em {}.'.format(x, y, anohoje+y))
elif x == 18:
    print('{} anos. É hora de se alistar.'.format(x))
else:
    print('{} anos. Você já passou da idade de alistamento. Se passaram {} anos, você deveria ter se alistado em {}.'.format(x, z, anohoje-z))
