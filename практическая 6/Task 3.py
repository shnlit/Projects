column_1, row_1 = map(int, input("Введите номер столбца и строчки для 1 точки (от 1 до 8): ").split())
column_2, row_2 = map(int, input("Введите номер столбца и строчки для 2 точки (от 1 до 8): ").split())

if (
    column_1 >= 1 and column_1 <= 8 and column_2 >= 1 and column_2 <= 8
    and row_1 >= 1 and row_1 <= 8 and row_2 >= 1 and row_2 <= 8
):
    if (column_1 % 2 != 0 and row_1 % 2 != 0) or (column_1 % 2 == 0 and row_1 % 2 == 0):
        color_1 = 'white'
    else:
        color_1 = 'black'
    if (column_2 % 2 != 0 and row_2 % 2 != 0) or (column_2 % 2 == 0 and row_2 % 2 == 0):
        color_2 = 'white'
    else:
        color_2 = 'black'
    if color_1 == color_2:
        print('YES')
    else:
        print('NO')
else:
    print('Ошибка ввода')