year = int(input('Введите порядковый номер месяца: '))

if  year == 2:
    print('В этом месяце 28 дней')
elif (
    (year % 2 != 0 and 1 <= year <= 7) or
    (year % 2 == 0 and 8 <= year <= 12)
):
    print('В этом месяце 31 дней')
elif (
    (year % 2 != 0 and 8 <= year <= 12) or
    (year % 2 == 0 and 1 <= year <= 7)
):
    print('В этом месяце 30 дней')
else:
    print('Ошибка')