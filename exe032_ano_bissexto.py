# feito utilizando a aula, porque eu não sabia fazer
from datetime import date
ano = int(input('Digite o ano a ser analisado [Digite 0 para o atual]: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} é NÃO É BISSEXTO.'.format(ano))
