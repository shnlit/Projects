side_1 = int(input('Введите первую сторону треугольника: '))
side_2 = int(input('Введите вторую сторону треугольника: '))
side_3 = int(input('Введите третью сторону треугольника: '))

if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
    if side_1 == side_2 == side_3:
        print('Равносторонний')
    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print('Такого треугольника не существует')
