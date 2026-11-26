import random

status = input("Введите статус заказа: ")

match status:
    case "pending":
        status = "В ожидании ⏳"
        desc = "Ваш заказ создан и ожидает подтверждения"
        wait_time = f"{random.randint(1, 10)} минут"
        advice = "Пожалуйста, дождитесь подтверждения оператора"
    case "processing":
        status = "В обработке ⚙️"
        desc = "Ваш заказ обрабатывается и готовится к отправке"
        wait_time = f"{random.randint(1, 3)} часов"
        advice = "МЫ уведомим вас, когда заказ будет передан в доставку"
    case "shipped":
        status = "Отправлено ✈️"
        desc = "Заказ передан курьерской службе и находится в пути"
        wait_time = f'{random.randint(2, 5)} дней'
        advice = "Следите за уведомлениями о доставке"
    case "delivered":
        status = "Доставлено ✅"
        desc = "Заказ успешно доставлен и готов к получению"
        wait_time = "0 минут"
        advice = "Можете прийти и забрать заказ в любой момент"
    case "cancelled":
        status = "Отменено ❌"
        desc = "Заказ был отменен по вашей или нашей инициативе"
        wait_time = 'Не применимо'
        advice = "Ваши средства вернутся вам в течении 3 рабочих дней"
    case _:
        print(
            """❌ Ошибка: Неизвестный статус "invalid_status"
Доступные статусы: pending, processing, shipped, delivered, cancelled""")
        exit()

print("""
╔════════════════════════════════════╗
‖     📦 СТАТУС ВАШЕГО ЗАКАЗА 📦     ‖
╚════════════════════════════════════╝""")
print(f""" 
Статус: {status}
Описание: {desc}
Примерное время: {wait_time}
Рекомандация: {advice}""")



