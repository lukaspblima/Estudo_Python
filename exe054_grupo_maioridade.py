from datetime import date
hoje = int(date.today().year)
print('Identificador de Maioridade')
n = int(input('Quantas pessoas deseja analisar: '))
pessoa = []
nascimento = []
for c in range(0, n):
    nome = input('Digite o nome da {}ª pessoa: '.format(c+1))
    pessoa.append(nome)
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c+1)))
    nascimento.append(nasc)
print('='*20)
mai = 0
men = 0
for c in range(0, n):
    i = hoje-nascimento[c]
    if i>=21:
       mai += 1
        print('{} possui {} anos, sendo então MAIOR DE IDADE.'.format(pessoa[c], i))
    else:
        men += 1
        print('{} possui {} anos, sendo então MENOR DE IDADE.'.format(pessoa[c], i))
print('Ao todo são {} indivíduos maiores de idade e {} menores de idade.'.format(mai, men))

