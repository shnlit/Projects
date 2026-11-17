gas_price = 49.5


def calculate_fuel_cost(distance, fuel_consumption):
    """Рассчитывает количество топлива и его стоимость."""

    fuel_needed = distance * (fuel_consumption / 100)
    total_cost = fuel_needed * gas_price

    return fuel_needed, total_cost

distance = float(input("Введите расстояние (км): "))
fuel_consumption = float(input("Введите расход топлива на 100 км: "))

fuel_needed, total_cost = calculate_fuel_cost(distance, fuel_consumption)

print(f"Необходимое кол-во топлива: {fuel_needed:.2f} л")
print(f"Стоимость поездки: {total_cost:.2f} руб.")