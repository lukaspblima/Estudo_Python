print('{:=^30}'.format(' REGISTRADOR DE COMPRAS '))
mais1k = maisbaratop = total = qtd = 0
mbaraton = ''
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço do produto [R$]: '))
    total += preco
    qtd += 1
    if preco > 1000:
        mais1k += 1
    if maisbaratop == 0:
        mbaraton = prod
        maisbaratop = preco
    elif preco < maisbaratop:
        mbaraton = prod
        maisbaratop = preco
    cont = str(input('CONTINUAR? [S/N]: '))
    while cont not in 'SsNn':
        cont = str(input('CONTINUAR? [S/N]: '))
    if cont in 'Nn':
        break
print('{:=^30}'.format(' FIM DAS COMPRAS '))
print(f'Total de itens: {qtd}.')
print(f'Total do preço: R${total:.2f}.')
print(f'Total de {mais1k} produtos custam mais de R$ 1 mil.')
print(f'O produto mais barato é "{mbaraton}", custando R${maisbaratop:.2f}.')
