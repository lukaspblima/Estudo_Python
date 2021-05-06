from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(numeros)
print(f'O maior número é: {sorted(numeros)[0]}')
print(f'O menor número é: {sorted(numeros)[-1]}')