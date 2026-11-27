COFFEE_PRICE = 120
TEA_PRICE = 80
JUICE_PRICE = 100
WATER_PRICE = 50
LEMONADE_PRICE = 90

STUD_DISCOUNT = 0.8
ADMIN_DISCOUNT = 0.5
OLD_DISCOUNT = 0.7



drink = input('Введите название или номер напитка: ').strip().lower()
amount = int(input('Введите количество напитков: '))
discount_code = input('Введите код скидки (при наличии) или нажмите ENTER: ')
match drink:
    case "кофе" | '1':
        emoji = '☕'
        total = COFFEE_PRICE * amount
        drink = 'Кофе'
        price = COFFEE_PRICE
    case "чай" | '2':
        emoji = '🍵'
        total = TEA_PRICE * amount
        drink = 'Чай'
        price = TEA_PRICE
    case "сок" | '3':
        emoji = '🧃'
        total = JUICE_PRICE * amount
        drink = 'Сок'
        price = JUICE_PRICE
    case "вода" | '4':
        emoji = '💧'
        total = WATER_PRICE * amount
        drink = 'Вода'
        price = WATER_PRICE
    case "лимонад" | '5':
        emoji = '🍋'
        total = LEMONADE_PRICE * amount
        drink = 'Лимонад'
        price = LEMONADE_PRICE
    case _:
        print('❌Ошибка ввода напитка❌')
        exit()

match amount:
    case 1:
        portions = 'порция'
    case 2 | 3 | 4:
        portions = 'порции'
    case _:
        if amount >= 5:
            portions = 'порций'
        else:
            print('❌Ошибка ввода количества порций❌')
            exit()

match discount_code:
    case 'STUDENT':
        end_total = total * STUD_DISCOUNT
        discount_sum = total - end_total
        discount_text = f'Скидка "STUDENT" (20%): -{discount_sum:.0f} руб '
    case 'ADMIN':
        end_total = total * ADMIN_DISCOUNT
        discount_sum = total - end_total
        discount_text = f'Скидка "ADMIN" (50%): -{discount_sum:.0f} руб '
    case 'OLD':
        end_total = total * OLD_DISCOUNT
        discount_sum = total - end_total
        discount_text = f'Скидка "OLD" (30%): -{discount_sum:.0f} руб '
    case '':
        end_total = total
        discount_sum = ''
        discount_text = ''
    case _:
        print('❌Такого кода не существует❌')
        end_total = total
        discount_sum = ''
        discount_text = ''

print(f"""
╔════════════════════════════════════╗
‖       {emoji} КВИТАНЦИЯ КАФЕ {emoji}        ‖
╚════════════════════════════════════╝

Товар: {drink} {emoji}
Цена за порцию: {price} руб
Количество: {amount} {portions}
Сумма: {total:.0f} руб

{discount_text}
═══════════════════════════════════════
💰 К ОПЛАТЕ: {end_total:.0f} руб
═══════════════════════════════════════
""")
