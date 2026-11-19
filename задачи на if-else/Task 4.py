weight = int(input('Введите вес боксёра: '))

if weight < 60:
    print('Боксёр в лёгком весе')
elif 60 <= weight < 64:
    print('Боксёр в первом полусреднем весе')
elif 64 <= weight < 69:
    print('Боксёр в полусреднем весе')
else:
    print('Ошибка')