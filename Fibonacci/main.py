def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 2) + fibonacci(i - 1)

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input(f'Digite um número: '))

for x in range(n):
    print(fibonacci(x))
