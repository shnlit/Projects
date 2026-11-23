col_1, row_1 = map(int, input('Введите номер столбца и строчки для 1 точки (от 1 до 8): ').split())
col_2, row_2 = map(int, input('Введите номер столбца и строчки для 2 точки (от 1 до 8): ').split())

if not (1 <= col_1 <= 8 and 1 <= row_1 <= 8 and 1 <= col_2 <= 8 and 1 <= row_2 <= 8):
  print('Ошибка ввода')
elif (col_1 + row_1) % 2 == (col_2 + row_2) % 2:
  print('YES')
else:
  print('NO')