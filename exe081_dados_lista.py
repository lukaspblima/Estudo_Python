print('Leitor de Dados de uma Lista')
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    c = str(input('Continuar [S/N]: '))
    if c in 'SsNn':
        if c in 'Nn':
            break
    else:
        lista.append(int(input('Erro! Digite um número: ')))
lista.sort(reverse=True)
print(f'Quantidade de dados inseridos: {len(lista)}')
print(f'Valores inseridos de forma decrescente: {lista}') # tá dando errado, não sei porque
print(f'Quantidade de eventos do nº 5: ', end='')
c = 0
for v in lista:
    if v == 5:
        c += 1
print(c, end=' ')