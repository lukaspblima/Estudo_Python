tupla = ('Caneta ', 3.50,
         'Lapiseira ', 5.29,
         'Caderno ', 15.90,
         'Livro ', 49.70,
         'Borracha ', 2.99)
print(f'====={"LISTA DE PREÇOS" :^29}=====')
for posicao in range (0, len(tupla)):
    if posicao%2 == 0: # na tupla, os itens estão em posição PAR, os preços em IMPAR
        print(f'{tupla[posicao]:.<30}', end=' ')
    else:
        print(f'R${tupla[posicao]:>6.2f}')
