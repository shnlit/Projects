color_1 = input('Введите 1-ый цвет: ')
color_2 = input('Введите 2-ой цвет: ')

if (color_1 == 'красный' or color_2 == 'красный') and (color_1 == 'синий' or color_2 == 'синий'):
    print('Получился фиолетовый')
elif (color_1 == 'красный' or color_2 == 'красный') and (color_1 == 'желтый' or color_2 == 'желтый'):
    print('Получился оранжевый')
elif (color_1 == 'синий' or color_2 == 'синий') and (color_1 == 'желтый' or color_2 == 'желтый'):
    print('Получился зеленый')
else:
    print('Ошибка')