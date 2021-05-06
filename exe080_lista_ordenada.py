print('Lista Ordenada (sem o "sort")')
lista = []
for c in range(1, 6):
    n = int(input(f'Digite o {c}º valor: '))
    if c == 1 or n >= max(lista):
        lista.append(n)
    else:
        if n <= min(lista):
            lista.insert(0, n)
        elif n > min(lista) and n < max(lista):
            for x in range(1, len(lista)):
                if n >= lista[x] and n < lista[x+1]:
                    lista.insert(x, n)
                    break

print(lista)
