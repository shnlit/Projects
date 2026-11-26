import random
from turtledemo.round_dance import stop

status = input("Введите статус заказа: ")

wait_1 = random.randint(0, 5)
wait_2 = random.randint(6, 10)

print("""
╔════════════════════════════════════╗
‖     📦 СТАТУС ВАШЕГО ЗАКАЗА 📦     ‖
╚════════════════════════════════════╝
""")

match status:
    case "pending":
        status = "В ожидании"
        desc = "Ждем подтверждение оплаты заказа"
    case "processing":
        status = "В обработке"
        desc = "Ваш заказ обрабатывается и готовится к отправке"
    case "shipped":
        status = "Отправлено"
        desc = "Заказ передан курьерской службе и находится в пути"
    case "delivered":
        status = "доставлено"
        desc = "Заказ успешно доставлен и готов к получению"
    case "cancelled":
        status = "Отменено"
        desc = "Заказ был отменен по вашей или нашей инициативе"

    case _ :
        print(
            """❌ Ошибка: Неизвестный статус "invalid_status"
Доступные статусы: pending, processing, shipped, delivered, cancelled""")

print(f""" 
Статус: {status}
Описание: {desc}
Примерное время: от {wait_1} - {wait_2}
Рекомандация: Следите за уведомлениями о доставке





""")



