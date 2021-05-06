print('Analise os Parênteses de uma expressão')
e = str(input('Digite a expressão: '))
"""pa = 0
pf = 0
for v in e:
    if v == '(':
        pa += 1
    if v == ')':
        pf += 1
if pa == pf:
    print('A expressão é válida! Todos os parênteses fechados.')
else:
    print('A expressão não é válida! Algum parêntese não foi fechado.')"""
lista = []
for s in e:
    if s == '(':
        lista.append('(')
    elif s ==')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão é válida! Todos os parênteses fechados.')
else:
    print('A expressão não é válida! Algum parêntese foi mal colocado.')