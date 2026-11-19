temperature = float(input('Введите температуру (℃): '))
pressure = int(input('Введите давление (верхнее): '))
pulse = int(input('Введите пульс (уд/мин): '))

if 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60  <= pulse <= 100:
    print('Вы в порядке')

elif (
    (35 <= temperature <= 36 or 37 <= temperature <= 38)
    or (105 <= pressure <= 110 or 130 <= pressure <= 140)
    or (55  <= pulse <= 60 or 100  <= pulse <= 110)
):
    print('У вас лёгкое недомогание')

elif (
    (temperature < 35 or temperature > 38)
    or (pressure < 105 or pressure > 140)
    or (pulse < 50 or pulse > 110)
):
    print('Вам срочно требуется врач')

print('Уточнить условие у препода')
