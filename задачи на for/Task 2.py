factorial = 1
n = int(input('Введите n: '))

for i in range(1, n+1):
    factorial *= i
print(factorial)