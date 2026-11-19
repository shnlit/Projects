pocket_num = int(input('Введите номер кармана: '))

if 0 <= pocket_num <= 36:
    if pocket_num == 0:
        print('Ваш карман - зелёный')
    elif pocket_num % 2 != 0:
        if  1 <= pocket_num <= 10 or 19 <= pocket_num <= 28:
            print('Ваш карман - красный')
        elif  11 <= pocket_num <= 18 or 29 <= pocket_num <= 36:
            print('Ваш карман - чёрный')
    elif pocket_num % 2 == 0:
        if  11 <= pocket_num <= 18 or 29 <= pocket_num <= 36:
            print('Ваш карман - красный')
        elif  1 <= pocket_num <= 10 or 19 <= pocket_num <= 28:
            print('Ваш карман - чёрный')
else:
    print('Ошибка ввода')