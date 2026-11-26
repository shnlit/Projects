num_1 = float(input('Введите первое число: '))
oper = input('Введите операцию: ')
num_2 = float(input('Введите второе число: '))

match oper:
    case '+':
        result = num_1 + num_2
        print(f'{num_1} {oper} {num_2} = {result}')
    case '-':
        result = num_1 - num_2
        print(f'{num_1} {oper} {num_2} = {result}')
    case '*':
        result = num_1 * num_2
        print(f'{num_1} {oper} {num_2} = {result}')
    case '/':
        if num_2 == 0:
            print('Ошибка: деление на ноль')
        else:
            result = num_1 / num_2
            print(f'{num_1} {oper} {num_2} = {result}')
    case _:
        print('Неизвестная операция')