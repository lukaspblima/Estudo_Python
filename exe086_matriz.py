matriz = [[], [], []]
for c in range(1, 10):
    n = int(input(f'Digite o {c}º número: '))
    if c < 4:
        matriz[0].append(n)
    elif c > 3 and c < 7:
        matriz[1].append(n)
    else:
        matriz[2].append(n)
"""for v in matriz[0]:
    print(f'[ {v} ]', end=' ')
print()
for v in matriz[1]:
    print(f'[ {v} ]', end=' ')
print()
for v in matriz[2]:
    print(f'[ {v} ]', end=' ')"""
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[ {matriz[a][b]:^5} ]', end=' ')
    print()