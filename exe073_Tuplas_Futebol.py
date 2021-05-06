times = ('flamengo', 'botafogo', 'fluminense', 'vasco', 'corinthians', 'palmeiras', 'grêmio', 'são paulo', 'curitiba', 'cruzeiro', 'portuguesa')
print(f'Os primeiros 5 colocados são: ', end='')
for t in range(0, 6):
    print(times[t].capitalize(), ', ' if t < 5 else '.', end='')
print(f'\nOs últimos 4 colocados são: ', end='')
for t in range(-1, -5, -1):
    print(times[t].capitalize(), ', ' if t > -4 else '.', end='')
print(f'\nOs times em ordem alfabética são: ', end='')
for t in sorted(times):
    print(t.capitalize(), end='; ')
print(f'\nO time "Corinthians" está na posição: {times.index("corinthians")+1}')
